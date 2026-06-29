import os

from dotenv import load_dotenv

from api_client import ApiClient

load_dotenv()


BASE_URL = (
    "https://zvyhufnwclhcvmgtqxwp."
    "supabase.co/functions/v1/api-v1"
)


def main():

    client = ApiClient(BASE_URL)

    auth = client.authenticate(
        os.getenv("LOGIN_USERNAME"),
        os.getenv("LOGIN_PASSWORD")
    )

    client.verify_mfa(
        auth["mfa_token"],
        os.getenv("MFA_CODE")
    )

    banking = client.update_banking(
        "123456789",
        "123456789012"
    )

    payment = client.update_payment(
        "Test user",
        "4242424242424242",
        "12",
        "2030",
        "123"
    )

    print("Banking updated:")
    print(banking)

    print("\nPayment updated:")
    print(payment)


if __name__ == "__main__":
    main()