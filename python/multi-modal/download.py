# leave here for future improvment
import urllib
from bs4 import BeautifulSoup
import mechanize


def getSearch(query):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent', 'chrome')]
	url = 'https://www.google.com/search?source=lnms&tbm=isch&sa=X&q=' + query
	print 'url: ', url
	html = browser.open(url).read()
	f = open('d.txt', 'w')
	f.write(html)
	img_urls = []
	titles = []
	res0 = html.split('imgurl')[1:]
	print res0
	for it in res0:
		res1 = it.split('&'[0])[0]
		print res1	
	
getSearch('cat')
