import config_manager
import global_config

cfg = global_config.GlobalConfig()
config = config_manager.ConfigManager(cfg.rootConfigPath)
