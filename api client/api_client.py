import requests

from exceptions import (
    AuthenticationError,
    MFAError,
    ValidationError,
    RateLimitError
)

class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def _handle_errors(self, response):

        if response.status_code == 401:
            raise AuthenticationError(
                "Invalid username or password."
            )

        if response.status_code == 403:
            raise MFAError(
                "Invalid MFA code."
            )

        if response.status_code == 422:
            raise ValidationError(
                f"Validation error: {response.text}"
            )

        if response.status_code == 429:
            raise RateLimitError(
                "Rate limit exceeded. Please try again later."
            )

        # Handle any other unexpected errors
        response.raise_for_status()

    def authenticate(self, username, password):

        response = self.session.post(
            f"{self.base_url}/auth/token",
            json={
                "email": username,
                "password": password
            }
        )

        self._handle_errors(response)

        return response.json()

    def verify_mfa(self, temp_token, code):

        response = self.session.post(
            f"{self.base_url}/auth/mfa/verify",
            headers={
                "Authorization": f"Bearer {temp_token}"
            },
            json={"mfa_token": temp_token, "code": code}
        )

        self._handle_errors(response)

        token = response.json()["access_token"]

        self.session.headers.update(
            {"Authorization": f"Bearer {token}"}
        )

    def update_banking(self, routing, account):

        response = self.session.put(
            f"{self.base_url}/account/banking",
            json={
                "routing_number": routing,
                "account_number": account
            }
        )

        self._handle_errors(response)

        return response.json()

    def update_payment(
            self,
            cardholder,
            card_number,
            expiry_month,
            expiry_year,
            cvc):

        response = self.session.put(
            f"{self.base_url}/account/payment",
            json={
                "cardholder_name": cardholder,
                "card_number": card_number,
                "exp_month": expiry_month,
                "exp_year": expiry_year,
                "cvc": cvc
            }
        )

        self._handle_errors(response)

        return response.json()