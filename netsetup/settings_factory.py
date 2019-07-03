from pkg_resources import resource_string

import json

class SettingsFactory():
    @staticmethod
    def create(filename):
        with resource_string(__name__, filename) as json_file:
            settings = json.loads(json_file)

        return settings
