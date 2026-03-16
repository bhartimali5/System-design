### Example of Singleton with intialization check (only once)

class ConfigParser:

    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = {}
            cls._instance.hasLoaded = False
        return cls._instance
    
    def load_config(self, config):
        if self._instance.hasLoaded:
            print("Config already loaded, skipping.")
            return
        self._instance._config = config
        self._instance.hasLoaded = True
        return self._instance._config
    
cfg = ConfigParser()
cfg.load_config({"db_host": "localhost", "db_port": 5432})
print(cfg._config)
cfg2 = ConfigParser()
cfg2.load_config({"db_host": "remotehost", "db_port": 3306})
print(cfg2._config)
