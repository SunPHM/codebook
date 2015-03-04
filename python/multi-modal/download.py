# leave here for future improvment
import urllib
from bs4 import BeautifulSoup
import mechanize


def getSearch(query):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent', 'chrome')]
	url = 'https://www.google.com/search?q=' + query + '&es_sm=122&source=lnms&tbm=isch&sa=X&biw=1301&bih=611i'
	print 'url: ', url
	html = browser.open(url)
	soup = BeautifulSoup(html)
	print type(soup)
	l = soup.find_all('img')
	for x in l:
		print x
	#f = open('d.txt', 'w')
	#f.write(soup)
	#img_urls = []
	#titles = []
	#res0 = soup.split('imgurl')[1:]
	#print res0
	#for it in res0:
	#	res1 = it.split('&'[0])[0]
	#	print res1	
	
getSearch('cat')
