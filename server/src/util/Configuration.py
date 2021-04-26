import json

class Configuration:

    def __init__(self):

        with open("application.json") as file:
            self.config = json.loads(file.read())
    
    def get(self, configName):
        return self.config[configName]
