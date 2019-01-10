'''
This class contains all functions related to the driver
'''
from selenium import webdriver
import os, sys
from utilities.utilities import Utilities

class DriverProvider:
    driver_provider = None



    def __init__(self, browser='chrome'):
        if sys.platform == "win32":
            chrome = '\chromedriver.exe'
        else:
            chrome = '/chromedriver'
        utilities = Utilities()
        # path = utilities.move_up_directory(os.getcwd(), 1)
        currentFilePath = os.path.realpath(__file__)
        new_path = utilities.move_up_directory(currentFilePath, 1)
        print(new_path + chrome)
        if browser.lower() == 'chrome':
            self.driver_provider = webdriver.Chrome(new_path + chrome)
        elif browser.lower() == 'firefox':
            self.driver_provider = webdriver.Firefox()