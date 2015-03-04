# leave here for future improvment
import urllib
from bs4 import BeautifulSoup
import mechanize


def getSearch(query):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent', 'Chrome')]
	url = 'https://www.google.com/search?es_sm=122&source=lnms&tbm=isch&sa=X&q=' + query
	html = browser.open(url)
	print html
	
	
getSearch('cat')
