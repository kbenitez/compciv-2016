import os
import requests

os.makedirs("tempdata", exist_ok = True)

resp = requests.get("http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt")

# assuming the subdirectory tempdata has been created:
zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")
babesfile = open(zname, "w")
babesfile.write(resp.text)
text = resp.text


numChars = 0
for line in text:
    numChars += len(line)

print("There are", numChars, "characters in", zname)

babesfile.close()