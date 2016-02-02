import os
import requests

os.makedirs("tempdata", exist_ok = True)

resp = requests.get("http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt")

# assuming the subdirectory tempdata has been created:
zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")
babesfile = open(zname, "w")
babesfile.write(resp.text)

numLines = len(resp.text.splitlines())
print("There are", numLines, "lines in", zname)

babesfile.close()