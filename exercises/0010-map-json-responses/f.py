import json
import os

f = open((os.path.join('tempdata', 'mapzen', 'stanford.json')), 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
print("type: " + mydict["type"]) 
print("text: " + mydict["geocoding"]["query"]["text"])
print("size: " + str(mydict["geocoding"]["query"]["size"]))
print("boundary.country: " + mydict["geocoding"]["query"]["boundary.country"])
