from pprint import pprint 
from config import ConfigManager
from global_config import GlobalConfig

cfg = GlobalConfig()

cmgr = ConfigManager(cfg.rootConfigPath)
print(type(cmgr.root.root))
pprint(cmgr.root.root)

