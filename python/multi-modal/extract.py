import urllib
import simplejson

def extractData(category):
	# get top 200 queries for one category
	num_queries = 16 * 4  
	query = urllib.urlencode({'q' : category})
	url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + category

	for start in range(0, num_queries, 4):
    		request_url = '{0}&start={1}'.format(url, start)
    		search_results = urllib.urlopen(request_url)
    		json = simplejson.loads(search_results.read())
    		#if json['responseData'] != None:
		results = json['responseData']['results']
    		for i in results:
        		print i['title'] + ": " + i['url']
		#else: print start
extractData('cat')
#extractData('dog')
