from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CHECKOUT = (By.ID, "checkout")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    ELEMENT_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_WITHOUT_ITEMS = 0
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def remove_product(self):        
        self.click(*self.REMOVE_BACKPACK)

    def get_cart_badge_count(self):
        badge = self.wait_element(*self.ELEMENT_BADGE)            

        if badge is None:            
            return int(self.CART_WITHOUT_ITEMS)
        else:
            return int(badge.text) if badge else 0    

    def continue_cart(self):
        self.click(*self.CONTINUE_SHOPPING_BUTTON)
       
    def return_to_inventory(self):
        self.driver.back()