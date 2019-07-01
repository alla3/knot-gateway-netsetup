import json
import os

import logging

class SettingsFactory():
    @staticmethod
    def create(filename):
        print os.getcwd()
        with open(filename) as json_file:
            settings = json.load(json_file)

        return settings
