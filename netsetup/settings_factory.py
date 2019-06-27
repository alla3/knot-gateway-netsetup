import json
import os

class SettingsFactory():
    @staticmethod
    def create(filename):
        ## print os.listdir(os.getcwd())
        print os.getcwd()
        with open(filename) as json_file:
            settings = json.load(json_file)
            #pass
        #open(filename) as json_file
        #return json.loads(filename)
        return settings
