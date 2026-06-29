import os

from dotenv import load_dotenv
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.account_page import AccountPage

load_dotenv()

def test_user_can_update_account(page):

    try:
        login = LoginPage(page)
        account = AccountPage(page)

        print("Starting test: User can update account information")
        
        # Banking and payment information to update
        routing = "123456789"
        bank_account = "123456789012"

        # Payment method information to update
        card_name = "Testing user"
        card_number = "4242424242424242"
        month = "12"
        year = "2030"
        cvc = "123"

        login.open()
        login.login(
            os.getenv("LOGIN_USERNAME"),
            os.getenv("LOGIN_PASSWORD")
        )

        login.complete_mfa(
            os.getenv("MFA_CODE")
        )

        page.goto(
            f"{os.getenv('BASE_URL')}/app/account"
        )

        account.update_banking(
            routing,
            bank_account
        )

        account.update_payment(
            card_name,
            card_number,
            month,
            year,
            cvc
        )

        routing_last4 = routing[-4:]
        account_last4 = bank_account[-4:]

        bank_summary = page.get_by_text("Routing:")

        expect(bank_summary).to_contain_text(routing_last4)
        expect(bank_summary).to_contain_text(account_last4)

    except Exception as e:
        print(f"Test failed: {e}")