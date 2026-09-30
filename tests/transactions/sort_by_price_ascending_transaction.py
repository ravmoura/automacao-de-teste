from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage

class SortByPriceAscendingTransaction(AbstractTransaction):
    
    def do(self):
        page = InventoryPage(self._driver)
        page.sort_by_price_ascending()
        
        elementos_preco = page.get_product_prices()

        # Remove the '$' symbol and convert to float
        precos_exibidos = [float(elemento.text[1:]) for elemento in elementos_preco]  
        return precos_exibidos == sorted(precos_exibidos)