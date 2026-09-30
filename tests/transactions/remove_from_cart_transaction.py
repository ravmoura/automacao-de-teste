from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage

class RemoveFromCartTransaction(AbstractTransaction):
    
    def do(self):
        page = InventoryPage(self._driver)
        page.add_product()
        page.go_to_cart()
        
        cart = CartPage(self._driver)        
        badgeCount = cart.get_cart_badge_count()

        if badgeCount == 1:
            cart.remove_product()
            badgeCount = 0
            cart.return_to_inventory()

        return badgeCount