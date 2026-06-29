class AccountPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(f"{self.page.url.split('/app')[0]}/app/account")

    def update_banking(self, routing, account):

        self.page.locator("#bank-routing").fill(routing)
        self.page.locator("#bank-account").fill(account)

        self.page.locator("#bank-save").click()

    def update_payment(self, name, card, month, year, cvc):

        self.page.locator("#card-holder").fill(name)
        self.page.locator("#card-number").fill(card)
        self.page.locator("#card-exp-month").fill(f"{month}")
        self.page.locator("#card-exp-year").fill(year)
        self.page.locator("#card-cvc").fill(cvc)

        self.page.locator("#card-save").click()

    def summary_text(self):
        return self.page.get_by_test_id(
            "last-updated-summary"
        )