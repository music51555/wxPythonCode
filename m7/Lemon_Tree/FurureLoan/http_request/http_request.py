import requests
import random
import settings

class HttpRequest:

    def __init__(self,url,data,cookies):
        self.url = url
        self.data = data
        self.cookies = cookies

    def get_headers(self):
        headers = {'UserAgent':random.choice(settings.USER_AGENT)}
        return headers

    def request_get(self):
        response = requests.get(url=self.url, params=self.data, headers = self.get_headers())
        return response

    def request_post(self):
        response = requests.post(url=self.url, data=self.data, cookies = self.cookies, headers = self.get_headers())
        return response