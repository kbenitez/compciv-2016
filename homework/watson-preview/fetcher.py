import os
import requests

os.makedirs("pics", exist_ok = True)

urls = ["https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Fall_Mickey_4x6_JTPI_5147_%2815268364538%29.jpg/1024px-Fall_Mickey_4x6_JTPI_5147_%2815268364538%29.jpg",
"https://upload.wikimedia.org/wikipedia/commons/0/06/Florida124.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Magic_Kingdom_Monorail_Entry_Arch.jpg/1024px-Magic_Kingdom_Monorail_Entry_Arch.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/MagicKindom-highres-park-cc.jpg/800px-MagicKindom-highres-park-cc.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/SophiaGrace%26Rosie.jpg/800px-SophiaGrace%26Rosie.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Walt_Disney_World_Gallery_Photo_%2812112912406%29.jpg/1024px-Walt_Disney_World_Gallery_Photo_%2812112912406%29.jpg"]

numUrls = len(urls)

for url in range(numUrls):
	resp = requests.get(urls[url])
	picname = "pic" + str(url) + ".jpg"
	zname = os.path.join("pics", picname)
	picFile = open(zname, "wb")
	picFile.write(resp.content)
	picFile.close()

