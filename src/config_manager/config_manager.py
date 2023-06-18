import json
import os

# from .config import Config
from .default_config import default_config


class ConfigManager:
    def __init__(self, root_path: str) -> None:
        # self.__cache = {}
        self.__root_path = os.path.expanduser(root_path)

    @property
    def root_path(self):
        return self.__root_path

    def make_default(self):
        """Make deafult config"""
        serialized = json.dumps(default_config, indent=4)

        if os.path.isfile(self.__root_path):
            answer = input(
                "Config file already exists, do you want to override it [y/N]?"
            )
            if answer != "y" and answer != "Y":
                return

        with open(self.__root_path, mode="w", encoding="utf-8") as file:
            file.write(serialized)

        print("The default config is written to: " + self.__root_path)

    # @property
    # def root(self):
    #     return self.getConfig('__root', self.__root_path)
    #
    # def getFirstExistedFile(self, pathList):
    #     for path in pathList:
    #         p = os.path.expanduser(path)
    #         if os.path.isfile(p):
    #             return p
    #
    #     raise Exception(f"Config file not found\nMake one of: {', '.join(self.__root_path)}")
    #
    # def getConfig(self, path, files = None):
    #     if path not in self.__cache:
    #         if files is None:
    #             f = path
    #         else:
    #             f = self.getFirstExistedFile(files)
    #         self.__cache[path] = Config(f)
    #
    #     return self.__cache[path]
    #
