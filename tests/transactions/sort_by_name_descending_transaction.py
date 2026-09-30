from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage

class SortByNameDescendingTransaction(AbstractTransaction):
    
    def do(self):
        page = InventoryPage(self._driver)
        page.sort_by_name_descending()
        
        elementos_nomes = page.get_product_names()
        nomes_exibidos = [elemento.text for elemento in elementos_nomes]
        return nomes_exibidos == sorted(nomes_exibidos, reverse=True)