from urllib.parse import urljoin
import requests as r


class Client:
    def __init__(self):
        self.url = 'http://127.0.0.1:5000/files/'

    def get_files(self):
        return r.get(self.url).json()

    def download_file(self, name):
        data = r.get(urljoin(self.url, name))
        with open(name, 'wb') as f:
            f.write(data.content)

    def upload_file(self, name):
        return r.post(self.url, files={'file': open(name, 'rb')})

    def delete_file(self, name):
        return r.delete(urljoin(self.url, name)).json()


c = Client()
print(c.download_file('text.txt'))
