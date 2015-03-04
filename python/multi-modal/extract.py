import urllib
import simplejson
import os

def extractData(category): # extract titles and links of images for one category from Google
	num_queries = 16 * 4  
	url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + category
	res = {}
	for start in range(0, num_queries, 4):
    		request_url = '{0}&start={1}'.format(url, start)
    		search_results = urllib.urlopen(request_url)
    		json = simplejson.loads(search_results.read())
		if json['responseData'] is not None:
			results = json['responseData']['results']
    			for item in results:
				title = item['titleNoFormatting'].lower()
        			if item['contentNoFormatting'].lower() not in title:
					title += ' ' + item['contentNoFormatting'].lower()
				#print item['titleNoFormatting']
				#print item['contentNoFormatting']
				image = item['url']
				if category in title:
					print title + ": " + image
					res[title] = image
	writeData(category, res)

def writeData(folder, d):
	if not os.path.exists(folder):
		os.makedirs(folder)
	f1 = open(folder + "/" + 'text.txt', 'w')
	n = 0
	for title in d:
		f1.write(title.encode('ascii', 'ignore') + "  :::  " + d[title].encode('ascii', 'ignore'))
		f1.write('\n')
		urllib.urlretrieve(d[title], folder + '/' + n + '.jpg')
		n += 1
	f1.close()


def genData(infile): # generate data by reading from a category.txt
	f = open(infile, 'r')
	for line in f:
		category = line[0 : len(line) - 1]
		print category
		extractData('data/' + category)
		

genData('category.txt')
#extractData('cat')
#extractData('dog')
#extractData('panda')
