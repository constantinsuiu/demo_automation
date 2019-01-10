'''
This class contains all functions related to the driver
'''
from selenium import webdriver
import os, sys
from utilities.utilities import Utilities

class DriverProvider:
    driver_provider = None

    def __init__(self, browser='chrome'):
        utilities = Utilities()
        path = utilities.move_up_directory(os.getcwd(), 1)
        if browser.lower() == 'chrome':
            self.driver_provider = webdriver.Chrome(path + '/utilities/chromedriver')
        elif browser.lower() == 'firefox':
            self.driver_provider = webdriver.Firefox()