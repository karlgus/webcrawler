#!/usr/bin/python3

from htmldom import htmldom


import re
import time

def getPage(url):
    dom = htmldom.HtmlDom(url).createDom()
    #find tag a
    a = dom.find("a")
    link = [link.attr("href") for link in a]
    unique_link = []
    [unique_link.append(path) for path in link if path not in unique_link]
    return unique_link
    #return [link.attr("href") for link in a]

class Link:
    '''This class will contain information about link object'''

    def __init__(self,url,*title):
        self.url = url
        #self.title = title
        self.linkstore = [url]

    def add_link_to_linkstore(self, url):
        self.linkstore.append(url)

    def get_linkstore(self):
        return self.linkstore

if __name__ == '__main__':

    #links = getPage('http://www.expressen.se')
    internal_links = ['/']
    #print(links)

    link = getPage('http://www.expressen.se' + internal_links[0])
    print(link)
    #links = []
    #[links.append(item) for item in link if item not in links]
    #for path in links:
    #    if re.match('^/',path):
    #        print(path)


#    for i in range(2):
#        time.sleep(1)
#        print('i = {0}'.format(i))
#        links = {i:getPage('http://aftonbladet.se' + internal_links[i-1][0])}
#    for i in range(1):
#        time.sleep(1)
#        print('i = {0}'.format(i))
#        links = {i:getPage('http://www.hd.se' + internal_links[i-1][i])}
#        print(links)
#        for internal in links:
#            print(internal)
#            #if re.match('(hd.se)',internal) == True or re.match('^/',internal):
#            if re.match('^/',internal):
#                internal_links.append(internal)

#    print(internal_links)

    #counter = 0
    #conf = True
    #while conf:
    #    print(counter)
    #    if counter == 2:
    #        conf = False
    #    print(conf)
    #    for l in links:
    #        #Controlling the new links
    #        if re.match("^/",l):
    #            print("This will be the path of the url: {0}".format(l))
    #            newurl = 'http://hd.se' + l
    #            print(newurl)
    #        print(counter)
    #        counter += 1