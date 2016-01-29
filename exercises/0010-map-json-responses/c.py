import json
import os

f = open((os.path.join('tempdata', 'googlemaps', 'stanford.json')), 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
 
numResults = len(mydict['results'])

for result in range(numResults):
	print(mydict['results'][result]['formatted_address'])