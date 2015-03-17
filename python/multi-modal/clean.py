# clean the dataset by removing unused title information and update the map.txt
import os

def clean(folder):
	subfolders = os.listdir(folder)
	for sf in subfolders:
		files = os.listdir(folder + '/' + sf)
		mt = folder + '/' + sf + '/map.txt'
		m = mtToMap(mt)
		print m
		#for f in files:
		#	if
 
def mtToMap (mt):
	f = open(mt, 'r')
	m = dict()
	index = 0
	for line in f:
		m[str(index) + '.jpg'] = line[0 : len(line) - 1]
		index += 1
	return m	

clean('/home/hadoop/Downloads/mmd-2')
