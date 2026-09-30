from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage

class SortByNameAscendingTransaction(AbstractTransaction):
    
    def do(self):
        page = InventoryPage(self._driver)
        page.sort_by_name_ascending()
        
        elementos_nomes = page.get_product_names()
        nomes_exibidos = [elemento.text for elemento in elementos_nomes]
        return nomes_exibidos == sorted(nomes_exibidos)