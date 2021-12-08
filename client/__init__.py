import requests as r
from urllib.parse import urljoin

class Client:
    def __init__(self):
        self.url = 'http://127.0.0.1:5000/files/'

    def getFiles(self):
        return r.get(self.url).json()

    def downloadFile(self, name):
        data = r.get(urljoin(self.url, name))
        with open(name, 'wb') as f: 
            f.write(data.content)

    def uploadFile(self, name):
        return r.post(self.url, files={'file': open(name, 'rb')})

    def deleteFile(self, name):
        return r.delete(urljoin(self.url, name)).json()


c = Client()
print(c.downloadFile('text.txt'))
