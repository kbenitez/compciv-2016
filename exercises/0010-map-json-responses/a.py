import os
import requests

os.makedirs("tempdata", exist_ok = True)
os.makedirs("tempdata/googlemaps", exist_ok = True)
os.makedirs("tempdata/mapzen", exist_ok = True)

print("---")
url = "http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json"
resp = requests.get(url)
print("Downloading from:", url)
# assuming the subdirectory tempdata has been created:
zname = os.path.join("tempdata", "googlemaps", "stanford.json")
geocodeFile = open(zname, "w")
print("Writing to:", zname)
geocodeFile.write(resp.text)

chars = len(resp.text)
numLines = len(resp.text.splitlines())
print("Wrote", numLines, "lines and", chars, "characters")

geocodeFile.close()
###############################################################
print("---")
url = "http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json"
resp = requests.get(url)
print("Downloading from:", url)
zname = os.path.join("tempdata", "mapzen", "stanford.json")
mapzenFile = open(zname, "w")
print("Writing to:", zname)
mapzenFile.write(resp.text)

chars = len(resp.text)
numLines = len(resp.text.splitlines())
print("Wrote", numLines, "lines and", chars, "characters")

mapzenFile.close()


