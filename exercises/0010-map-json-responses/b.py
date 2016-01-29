import json
import os

f = open((os.path.join('tempdata', 'googlemaps', 'stanford.json')), 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
print(mydict['status'])