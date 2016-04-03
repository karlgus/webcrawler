#!/usr/bin/python3

from htmldom import htmldom

import http.client
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
        self.linkstore = [url]

    def add_link_to_linkstore(self):
        pass

    def get_linkstore(self):
        return self.linkstore


if __name__ == '__main__':
    url = 'www.hd.se'
    data = openURL("http://www.hd.se")

    dom = htmldom.HtmlDom("www.hd.se").createDom()
    a = dom.find("a")
    for link in a:
        print(link.attr("href"))


