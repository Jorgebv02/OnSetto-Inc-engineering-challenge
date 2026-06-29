import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pytest

from api_client import ApiClient
from exceptions import AuthenticationError, MFAError, ValidationError, RateLimitError


class DummyResponse:
    def __init__(self, status_code=200, json_data=None, text=""):
        self.status_code = status_code
        self._json_data = json_data or {}
        self.text = text

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise Exception(f"HTTP {self.status_code}")


class DummySession:
    def __init__(self):
        self.headers = {}
        self.last_request = None

    def update(self, headers):
        self.headers.update(headers)

    def post(self, url, headers=None, json=None):
        self.last_request = {
            "method": "post",
            "url": url,
            "headers": headers,
            "json": json,
        }

        if url.endswith("/auth/mfa/verify"):
            return DummyResponse(200, json_data={"access_token": "mock-token"})

        return DummyResponse(200, json_data={"token": "mock-temp"})

    def put(self, url, json=None):
        self.last_request = {
            "method": "put",
            "url": url,
            "json": json,
        }
        return DummyResponse(200, json_data={"result": "ok"})


def test_authenticate_returns_json():
    client = ApiClient("https://example.com")
    client.session = DummySession()

    result = client.authenticate("user@example.com", "password123")

    assert result == {"token": "mock-temp"}
    assert client.session.last_request["method"] == "post"
    assert client.session.last_request["url"].endswith("/auth/token")
    assert client.session.last_request["json"] == {
        "email": "user@example.com",
        "password": "password123",
    }


def test_verify_mfa_updates_authorization_header():
    client = ApiClient("https://example.com")
    client.session = DummySession()

    client.verify_mfa("temp-token", "123456")

    assert client.session.headers["Authorization"] == "Bearer mock-token"


def test_update_banking_returns_json():
    client = ApiClient("https://example.com")
    client.session = DummySession()

    result = client.update_banking("123456789", "987654321")

    assert result == {"result": "ok"}
    assert client.session.last_request["method"] == "put"
    assert client.session.last_request["url"].endswith("/account/banking")
    assert client.session.last_request["json"] == {
        "routing_number": "123456789",
        "account_number": "987654321",
    }


def test_update_payment_returns_json():
    client = ApiClient("https://example.com")
    client.session = DummySession()

    result = client.update_payment(
        "Jane Doe",
        "4242424242424242",
        "12",
        "2030",
        "123",
    )

    assert result == {"result": "ok"}
    assert client.session.last_request["method"] == "put"
    assert client.session.last_request["url"].endswith("/account/payment")
    assert client.session.last_request["json"] == {
        "cardholder_name": "Jane Doe",
        "card_number": "4242424242424242",
        "exp_month": "12",
        "exp_year": "2030",
        "cvc": "123",
    }


@pytest.mark.parametrize(
    "status, exception_type",
    [
        (401, AuthenticationError),
        (403, MFAError),
        (422, ValidationError),
        (429, RateLimitError),
    ],
)
def test_handle_errors_raises_expected_exceptions(status, exception_type):
    client = ApiClient("https://example.com")
    response = DummyResponse(status_code=status, text="error")

    with pytest.raises(exception_type):
        client._handle_errors(response)
