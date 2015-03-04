# parse the existing html downloaded from Google search by hand
import os
import urllib

def parse(html, c, mmd):
	print c
	text = open(html, 'r').read()
	folder = mmd + '/' + c
 	if not os.path.exists(folder):
                os.makedirs(folder)
        out = open(folder + "/" + 'map.txt', 'w')
	res0 = text.split('imgurl=')[1:]
	imgurls = []
	for r in res0:
		ac = r.split('&')
		imgurls.append(ac[0])
	#print len(imgurls)
	titles = []
	res1 = text.split('"pt":"')[1:]
	for r in res1:
		titles.append(r.split('",')[0])
	#print len(titles)	
	n = 0
	an = 0
	for i in range(len(titles)):
		print str(n) + " : " + imgurls[i]
		suf = imgurls[i][-4:]
		if (suf == '.jpg'):
			out.write(titles[i] + "  ---  " + imgurls[i] + '\n')
			print imgurls[i]	
			try:
				urllib.urlretrieve(imgurls[i], folder + '/' + str(an) + '.jpg')
				out.write(titles[i] + "  ---  " + imgurls[i] + '\n')
				an += 1
			except:
				print 'this link ' + imgurls[i] + ' is corrupted or forbidden access'
		n += 1
	return
	
def read(file):
	f = open(file, 'r')
	cg = []
	for line in f:
		category = line[0: len(line) - 1]
		#print category
		cg.append(category)
	return cg

def main(inp, out):
	cg = read(inp)
	for c in cg:
		parse('data/' + c + '.html', c, out)

main('category.txt', 'mmd')
