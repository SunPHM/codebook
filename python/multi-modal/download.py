# leave here for future improvment
import bs4
from bs4 import BeautifulSoup

f = open('cat.html','r')
soup = BeautifulSoup(f.read())
#print soup.title
#print soup.prettify()
#f1 = open('a.html', 'w')
#f1.write(soup.find_all('a').str())
print soup.find_all('div', id='cnt', limit=10)
