from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ELEMENT_VISIBLE = (By.ID, "inventory_container")
    ELEMENT_ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com")
    
    def login(self, user, password):
        self.type(*self.USERNAME, user)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
        self.wait_element(*self.ELEMENT_VISIBLE)

    def login_error(self, user, password):
        self.type(*self.USERNAME, user)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
        msgError = self.wait_element(*self.ELEMENT_ERROR)

        return msgError.text

    def logout(self):
        self.driver.get("https://www.saucedemo.com/logout")