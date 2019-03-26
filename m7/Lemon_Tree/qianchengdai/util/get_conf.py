import configparser

class GetConf:

    def __init__(self,file_name,section,option):
        self.file_name = file_name
        self.section = section
        self.option = option
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file_name)

    def get_conf(self):
        value = self.conf.get(self.section,self.option)
        return value