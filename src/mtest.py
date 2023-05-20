from pprint import pprint 
from config_manager import ConfigManager

cmgr = ConfigManager()
print(type(cmgr.root.root))
pprint(cmgr.root.root)

