from guara.transaction import AbstractTransaction
from tests.pages.menu_page import MenuPage

class LogoutTransaction(AbstractTransaction):
    def do(self):        
        menu = MenuPage(self._driver)
        menu.logout()
        
        return self._driver.current_url