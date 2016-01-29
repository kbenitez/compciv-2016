import json
import os

f = open((os.path.join('tempdata', 'mapzen', 'stanford.json')), 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
 
numFeatures = len(mydict['features'])

for feature in range(numFeatures):
	labConCoord = ""
	labConCoord += ((mydict['features'][feature]['properties']['label']) + ";")
	labConCoord += (str(mydict['features'][feature]['properties']['confidence']) + ";")
	labConCoord += (str(mydict['features'][feature]['geometry']['coordinates'][0]) + ";") 
	labConCoord += (str(mydict['features'][feature]['geometry']['coordinates'][1]))
	print(labConCoord)