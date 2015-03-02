import urllib
import json

query = 'cat'
response = urllib.urlopen('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=cat').read()
res = json.loads(response)
#print res1

moreUrl = res['responseData']['cursor']['moreResultsUrl']
response1 = urllib.urlopen(moreUrl).read()
#res1 = json.loads(response1)

print response1

