import os

class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(os.getenv("BASE_URL") + "/login")

    def login(self, username, password):
        self.page.locator("#email").fill(username)
        self.page.locator("#password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()

    def complete_mfa(self, code):
        self.page.locator('input[autocomplete="one-time-code"]').fill(code)
        self.page.get_by_role("button", name="Verify").click()