import os

from config import Config
from global_config import GlobalConfig

class ConfigManager():
    def __init__(self) -> None:
        self.__cache = {}
        self.__globalConfig = GlobalConfig()

    @property
    def root(self):
        return self.getConfig('__root', self.__globalConfig.rootConfigPath)

    def getFirstExistedFile(self, pathList):
        for path in pathList: 
            p = os.path.expanduser(path)
            if os.path.isfile(p):
                return p

        raise Exception(f"Config file not found\nMake one of: {', '.join(self.__globalConfig.rootConfigPath)}")

    def getConfig(self, path, files = None):
        if path not in self.__cache:
            if files is None:
                f = path
            else:
                f = self.getFirstExistedFile(files)
            self.__cache[path] = Config(f)

        return self.__cache[path]

