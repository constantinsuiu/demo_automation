"""
This class contains all page objects that are present on all pages
(i.e. header, footer etc)
"""
from selenium.webdriver.common.by import By

class BasePage:
    driver = None
    _sign_in = {'by':By.CLASS_NAME, 'value': 'login'}
    _sign_out = {'by':By.CLASS_NAME, 'value':'logout'}

    def __init__(self, driver):
        self.driver = driver



    def set_text(self, text_box, text):
        self.driver.find_element(text_box['by'], text_box['value']).clear()
        self.driver.find_element(text_box['by'],text_box['value']).send_keys(text)

    def go_to(self, link):
        self.driver.find_element(link['by'], link['value']).click()