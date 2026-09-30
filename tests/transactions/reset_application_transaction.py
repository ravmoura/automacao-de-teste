from guara.transaction import AbstractTransaction
from tests.pages.cart_page import CartPage
from tests.pages.menu_page import MenuPage

class ResetApplicationTransaction(AbstractTransaction):
    def do(self):       
        menu = MenuPage(self._driver)
        menu.reset_application_state()

        cartShopping = CartPage(self._driver)        
        badgeCount = cartShopping.get_cart_badge_count()
        return badgeCount