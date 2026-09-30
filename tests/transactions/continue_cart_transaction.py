from guara.transaction import AbstractTransaction
from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage

class ContinueCartTransaction(AbstractTransaction):
    
    def do(self):            
        page = InventoryPage(self._driver)
        page.add_product()
        page.go_to_cart()
        
        cartShopping = CartPage(self._driver)          
        cartShopping.continue_cart()

        return self._driver.current_url
