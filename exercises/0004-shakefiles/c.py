import shutil
import os
import requests

zname = os.path.join("tempdata", "matty.shakespeare.tar.gz")
shutil.unpack_archive(zname, extract_dir = "tempdata")
print("Unpacked tempdata/matty.shakespeare.tar.gz into: tempdata")