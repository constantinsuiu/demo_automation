import unittest
from utilities.driver import DriverProvider
from utilities.config import Config



class TestHomePage(unittest.TestCase):
    driver = None
    config = None

    def setUp(self):
        try:
            self.driver = DriverProvider('chrome').driver_provider
            self.config = Config().config
            self.driver.get(self.config['baseURL'])
        except:
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()

    def test_check_title(self):
        assert("My Store" == self.driver.title)

if __name__ == "__main__":
    unittest.main()
