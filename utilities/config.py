'''
This file contains all Configuration data, like baseURL
'''
import json
import sys, os

class Config:
    config = None

    def __init__(self):
        current_path = self.move_up_directory(os.getcwd(), 1)
        with open(current_path + "\\utilities\\config.json", "r") as file:
            self.config = json.load(file)

    def move_up_directory(self, current_path, nr_of_moves):
        return "\\".join(current_path.split("\\")[:0-nr_of_moves])
