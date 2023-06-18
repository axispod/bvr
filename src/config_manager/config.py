import json

class Config:
    def __init__(self, path):
        with open(path, "r") as file:
            content = file.read()
            self.__config = json.loads(content)

    @property
    def root(self):
        return self.__config
    
