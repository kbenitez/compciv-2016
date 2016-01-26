import requests
import os

resp = requests.get("http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz")
print("Downloading: http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz")
# assuming the subdirectory tempdata has been created:
zname = os.path.join('tempdata', "matty.shakespeare.tar.gz")
Shakesfile = open(zname, "wb")
print("Writing file: tempdata/matty.shakespeare.tar.gz")
Shakesfile.write(resp.content)
Shakesfile.close()

