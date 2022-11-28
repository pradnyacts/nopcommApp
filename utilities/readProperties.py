import configparser
import os
config = configparser.ConfigParser()
ini_path = os.path.join(os.getcwd(), './Config/config.ini')
config.read(ini_path)
url = config.get('info', 'baseURL')
print(url)

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url= config.get('info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('info', 'password')
        return password
