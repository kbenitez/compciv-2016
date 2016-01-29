import json
import os

f = open((os.path.join('tempdata', 'googlemaps', 'stanford.json')), 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
 
numResults = len(mydict['results'])
for result in range(numResults):
	longName = ""
	numComponents = len((mydict['results'][result]['address_components']))
	for component in range(numComponents):
		longName += (mydict['results'][result]['address_components'][component]['long_name']) + "; "
	print(longName[:-2])