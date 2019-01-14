"""
This class contains all Page Objects for the Login page.
"""
from Page_Objects.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    _email_input = {'by':By.ID, 'value': 'email'}
    _password_input = {'by':By.ID, 'value': 'passwd'}
    _sign_in_button = {'by':By.ID, 'value': 'SubmitLogin'}

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)


    def login(self, username, password):
        self.set_text(self._email_input, username)
        self.set_text(self._password_input, password)
        self.driver.find_element(self._sign_in_button['by'], self._sign_in_button['value']).click()