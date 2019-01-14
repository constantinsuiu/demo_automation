import unittest
from utilities.driver import DriverProvider
from utilities.config import Config
from Page_Objects.BasePage import BasePage
from Page_Objects.Login_Page import LoginPage



class TestHomePage(unittest.TestCase):
    driver = None
    config = None
    base_page = None
    login_page = None

    def setUp(self):
        try:
            self.driver = DriverProvider('chrome').driver_provider
            self.config = Config().config
            self.driver.get(self.config['baseURL'])
            self.base_page = BasePage(self.driver)
            self.login_page = LoginPage(self.driver)

        except Exception as e:
            print(e)
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()

    def test_check_title(self):
        assert('My Store' == self.driver.title)

    def test_sign_in_link(self):
        self.base_page.go_to(self.base_page._sign_in)
        assert('Login - My Store' == self.driver.title)

    def test_login(self):
        username = self.config['user']
        password = self.config['password']
        self.base_page.go_to(self.base_page._sign_in)
        self.login_page.login(username, password)
        assert("Sign out" in self.driver.find_element(self.login_page._sign_out['by'], self.login_page._sign_out['value']).text)


if __name__ == "__main__":
    unittest.main()
