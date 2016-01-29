import json
import os

f = open((os.path.join('tempdata', 'googlemaps', 'stanford.json')), 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
 
numResults = len(mydict['results'])

for result in range(numResults):
	addressLocation = ""
	addressLocation += ((mydict['results'][result]['formatted_address']) + ";")
	addressLocation += (str(mydict['results'][result]['geometry']['location']['lng']) + ";")
	addressLocation += (str(mydict['results'][result]['geometry']['location']['lat'])) 
	print(addressLocation)