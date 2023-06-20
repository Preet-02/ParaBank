import configparser

config = configparser.RawConfigParser()

config.read("D:\\pythonProject\\ParaBank\\Configurations\\config.ini")


class ReadValue:
    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    
