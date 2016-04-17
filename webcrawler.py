#!/usr/bin/env python3

from htmldom import htmldom
import re
import time
import sys

link = []

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



def getPage(baseurl,currentdepth,urlpath=None):
#time.sleep(0.5)
	print("The currentdepth is: {0}".format(currentdepth))
	if currentdepth > 1:
		print(currentdepth)
		sys.exit()

	if urlpath == None:
		tmpurl = baseurl
	else:
		tmpurl = baseurl + urlpath
		print("the new tmpurl is: {0}".format(tmpurl))
	time.sleep(1)
	dom = htmldom.HtmlDom(tmpurl).createDom()

	a = dom.find("a")

	tmpLink = [tmpLink.attr("href") for tmpLink in a]

	unique_link = []
	# Adding new path from tmpLink if it not exist in unique_link already and if it's not in link that is the final variable to store all the links in
	[unique_link.append(path) for path in tmpLink if path not in unique_link and path not in link]

	for path in unique_link:
		if re.match("^/",path):
			print(path)


	print("This link is now followed: {0}".format(tmpurl))
	for path in unique_link:
		if re.match("^/",path):
			link.append(path)
			print(link)
			print("The next link to follow is {0}{1}".format(baseurl,path))
			getPage(baseurl,currentdepth,path)
	currentdepth=currentdepth+1
	print(link)


if __name__ == '__main__':
	getPage("http://www.norran.se",0)
