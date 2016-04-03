#!/usr/bin/python3

import http.client
import htmldom
import re
import time


def openURL(url,path="/"):
    conn = http.client.HTTPConnection(url)
    conn.request("GET",path)
    request = conn.getresponse()
    pagehtml = request.read()
    conn.close()
    return pagehtml

class Link:
    '''This class will contain information about link object'''

    def __init__(self,url,title):
        self.url = url
        self.title = title

    def add_link_to_linkstore(self):
        pass

    def get_linkstore(self):
        pass


if __name__ == '__main__':
    pass