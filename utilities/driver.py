'''
This class contains all functions related to the driver
'''
from selenium import webdriver

class DriverProvider:
    driver_provider = None

    def __init__(self, browser='chrome'):
        if browser.lower() == 'chrome':
            self.driver_provider = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver_provider = webdriver.Firefox()