import requests
import json
import urllib
from pprint import pprint


class RequestTemp():
    def __init__(self, url, header, payload, method):
        self.url = url
        self.header = header
        self.payload = payload
        self.method = method

    def send(self):
        payload = urllib.parse.urlencode(self.payload)
        if (self.method == "get"):
            res = requests.get(self.url+"?"+payload, headers=self.header)
        elif (self.method == "post"):
            res = requests.post(self.url, headers=self.header, data=payload)
        self.res = res
        self.res_content = res.content.decode("utf-8")

    def show_result(self):
        pprint(self.res_content, indent=2)
        
    def get_content(self, key):
        return self.res_content[key]
