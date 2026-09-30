from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage

class AddToCartTransaction(AbstractTransaction):
    
    def do(self):
        page = InventoryPage(self._driver)
        page.add_product()
        page.go_to_cart()
        
        cartShopping = CartPage(self._driver)        
        badgeCount = cartShopping.get_cart_badge_count()
        return badgeCount