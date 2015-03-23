# clean the dataset by removing unused title information and update the map.txt
import os
import shutil

def clean(infolder, outfolder):
	subfolders = os.listdir(infolder)
	for sf in subfolders:
		print 'handling ' + sf
		files = os.listdir(infolder + '/' + sf)
		mt = infolder + '/' + sf + '/map.txt'
		m = mtToMap(mt)
		if not os.path.exists(outfolder + '/' + sf):                                         
			os.makedirs(outfolder + '/' + sf)
		nmt = outfolder + '/' + sf + '/map.txt'
		output = open(nmt, 'w')
		#print m
		no = 0
		for f in files:
			if f != 'map.txt' and f != 'nmap.txt':
				filename = str(no) + '.jpg'
				output.write(filename  + '  ---  ' + m[f] + '\n')
				#print f, filename
				shutil.copy2(infolder + '/' + sf + '/' + f, outfolder + '/' + sf + '/' + filename)
				no += 1				
 
def mtToMap (mt):
	f = open(mt, 'r')
	m = dict()
	index = 0
	for line in f:
		splits = line[0 : len(line) - 1].split('  ---  ')
		#m[str(index) + '.jpg'] = line[0 : len(line) - 1]
		m[splits[0]] = splits[1] + '  ---  ' + splits[2]
		index += 1
	return m	

clean('lmm', 'lmm-1')
