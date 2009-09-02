from ConfigParser import ConfigParser

class DefaultConfigParser(ConfigParser):

    def get(self, section, key, default=None):
        if not self.has_option(section, key):
            return default
        return ConfigParser.get(self, section, key)

settings = DefaultConfigParser()
settings.read('config.ini')
