'''
This file contains all Configuration data, like baseURL
'''
import json
import sys, os
from utilities.utilities import Utilities


class Config:
    config = None
    utilities = Utilities()

    def __init__(self):
        # current_path = self.utilities.move_up_directory(os.getcwd(), 1)
        currentFilePath = self.utilities.move_up_directory(os.path.realpath(__file__), 1)
        with open(currentFilePath + "/config.json", "r") as file:
            self.config = json.load(file)


