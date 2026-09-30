from selenium.webdriver.common.by import By
from .base_page import BasePage

class MenuPage(BasePage):
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_APPLICATION_LINK = (By.ID, "reset_sidebar_link")

    def open_menu(self):
        self.click(*self.MENU_BTN)

    def logout(self):
        self.open_menu()
        elementLogout = self.wait_element(*self.LOGOUT_LINK)
        
        if elementLogout:
            self.click(*self.LOGOUT_LINK)
        

    def reset_application_state(self):
        self.open_menu()
        elementReset = self.wait_element(*self.RESET_APPLICATION_LINK)
        
        if elementReset:
            self.click(*self.RESET_APPLICATION_LINK)