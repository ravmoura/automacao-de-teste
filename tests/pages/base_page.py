from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)
    
    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        self.find(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text

    def wait_element(self, by, value):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
        except TimeoutException:
            return None

    def wait_for_page(self, url):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: url in driver.current_url
        )