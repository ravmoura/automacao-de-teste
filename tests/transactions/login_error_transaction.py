from guara.transaction import AbstractTransaction
from tests.pages.login_page import LoginPage

class LoginErrorTransaction(AbstractTransaction):
    
    def do(self, url, user, password):
        self._driver.get(url)

        page = LoginPage(self._driver)
        msgError = page.login_error(user, password)

        return msgError
