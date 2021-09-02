

import requests


class Request_Method_Package():

    def __init__(self):

        self.session = requests.session()
        self.url_invariant = 'https://test.ghparking.com:8080'


    def request_head(self,head=None):
        self.head = {"Content-Type":"application/json"}
        if head:
            self.session.headers.update(head)

    def SendRequest(self,method,url,**kwargs):
        self.url = self.url_invariant+url

        self.data = None
        if  'json' in kwargs:
            self.data = kwargs['json']
        #print(kwargs)
        self.res = self.session.request(method=method,url=self.url,json=self.data)
        self.response = self.res.json()

        if  'token_get' in kwargs:
            self.val = kwargs['token_get']
            self.get_token = self.response[self.val]['token']
            self.request_head({'X-Manage-Token':self.get_token})

        return self.response