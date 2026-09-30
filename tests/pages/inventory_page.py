from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    URL_INVENTORY = "https://www.saucedemo.com/inventory.html"
    URL_PART = "inventory.html"  
    COMBO_SORT = (By.CLASS_NAME, "product_sort_container")  
    SORT_OPTION_PRICE_ASCENDING = (By.XPATH, "//option[@value='lohi']")
    SORT_OPTION_PRICE_DESCENDING = (By.XPATH, "//option[@value='hilo']")
    SORT_OPTION_NAME_ASCENDING = (By.XPATH, "//option[@value='az']")
    SORT_OPTION_NAME_DESCENDING = (By.XPATH, "//option[@value='za']")
    PRICE_PRODUCTS = (By.CLASS_NAME, "inventory_item_price")
    NAME_PRODUCTS = (By.CLASS_NAME, "inventory_item_name")

    def is_loaded(self):
        self.wait_for_page(self.URL_PART)
        return (self.driver.current_url == self.URL_INVENTORY)
    
    def add_product(self):
        self.click(*self.ADD_BACKPACK)
    
    def go_to_cart(self):
        self.click(*self.CART)

    def get_product_prices(self):
        return self.find_elements(*self.PRICE_PRODUCTS)    

    def sort_by_price_ascending(self):
        self.click(*self.COMBO_SORT)
        self.click(*self.SORT_OPTION_PRICE_ASCENDING)
        
    def sort_by_price_descending(self):
        self.click(*self.COMBO_SORT)
        self.click(*self.SORT_OPTION_PRICE_DESCENDING)        

    def get_product_names(self):
        return self.find_elements(*self.NAME_PRODUCTS)

    def sort_by_name_ascending(self):
        self.click(*self.COMBO_SORT)
        self.click(*self.SORT_OPTION_NAME_ASCENDING)

    def sort_by_name_descending(self):
        self.click(*self.COMBO_SORT)
        self.click(*self.SORT_OPTION_NAME_DESCENDING)