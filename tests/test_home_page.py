import unittest
from utilities.driver import DriverProvider
from utilities.config import Config
from Page_Objects.BasePage import Header
from Page_Objects.Login_Page import Login_Page



class TestHomePage(unittest.TestCase):
    driver = None
    config = None
    base_page = None

    def setUp(self):
        try:
            self.driver = DriverProvider('chrome').driver_provider
            self.config = Config().config
            self.driver.get(self.config['baseURL'])
            self.login_page = Login_Page()

        except:
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()

    def test_check_title(self):
        assert('My Store' == self.driver.title)

    def test_sign_in_link(self):
        sign_in = self.driver.find_element_by_class_name(self.login_page.sign_in)
        sign_in.click()
        assert('Login - My Store' == self.driver.title)

    def test_login(self):
        sign_in = self.driver.find_element_by_class_name(self.login_page.sign_in)
        sign_in.click()
        email = self.driver.find_element_by_id(self.login_page.email_input)
        email.send_keys(self.config['user'])
        password = self.driver.find_element_by_id(self.login_page.password_input)
        password.send_keys(self.config['password'])
        submit = self.driver.find_element_by_id(self.login_page.sign_in_button)
        submit.click()
        sign_out = self.driver.find_element_by_class_name(self.login_page.sign_out)
        assert("Sign out" in sign_out.text)


if __name__ == "__main__":
    unittest.main()
