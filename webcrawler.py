#!/usr/bin/python3

from htmldom import htmldom


import re
import time

def getPage(url):
    dom = htmldom.HtmlDom(url).createDom()
    #find tag a
    a = dom.find("a")
    return set([link.attr("href") for link in a])

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


#link_targets = [link.attrib.get('href','') for link in doc.cssselect('a')]

    #url = 'http://www.hd.se'
    #dom = htmldom.HtmlDom({0}).createDom().format(url)
    #dom = htmldom.HtmlDom("http://www.hd.se").createDom()
    #a = dom.find( "a" )
    #links =  []
    #for link in a:
    #    print(link.attr("href"))
    #    links.append(link.attr("href"))

    #link = [link.attr("href") for link in a]

    #path = []
    #httpsurl = []
    #http = []

    #for url in link:
    #    if re.match("^/",url):
    #        path.append(url)
    #    if re.match("^https",str(url)):
    #        httpsurl.append(url)
    #    if re.match("^http://",str(url)):
    #        http.append(url)

    #print(http)

    links = getPage('http://www.hd.se')
    counter = 0
    conf = True
    while conf:
        print(counter)
        if counter == 2:
            conf = False
        print(conf)
        for l in links:
            #Controlling the new links
            if re.match("^/",l):
                print("This will be the path of the url: {0}".format(l))
                newurl = 'http://hd.se' + l
                print(newurl)
            print(counter)
            counter += 1

