import os
from pathlib import Path
import requests

class Storage:
    def __init__(self) -> None:
        self.__path = 'storage/'
    
    @staticmethod
    def convert(num):
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            
            num /= 1024.0
    
    def getFiles(self):
        return [{name: str(self.convert(os.stat(os.path.join(self.__path, name)).st_size))} for name in os.listdir(self.__path)]

    def getFile(self, name):
        return os.path.join(self.__path + name)

    def deleteFile(self, name: str):
        try:
            os.remove(os.path.join(self.__path, name))
            return True
        except FileNotFoundError:
            return False

    def uploadFile(self, file):
        if file.filename != ' ':
            file.save(os.path.join(self.__path + file.filename))
            return True
        
        return False
