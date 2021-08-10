from configparser import ConfigParser

class ReadConfig():

    def __init__(self,fileName):
        self.fileName = fileName

    def getData(self, section,key):
        config = ConfigParser()
        reader = config.read(self.fileName)
        return reader.get(section, key)

