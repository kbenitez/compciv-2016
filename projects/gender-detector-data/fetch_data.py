import requests
from os import makedirs
from os.path import join
from shutil import unpack_archive


SOURCE_URL = 'https://data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv?accessType=DOWNLOAD'
DATA_DIR = 'tempdata'
DATA_ZIP_PATH = join(DATA_DIR, 'chicago_employees.csv')
# make the directory
makedirs(DATA_DIR, exist_ok=True)

print("Downloading", SOURCE_URL)
resp = requests.get(SOURCE_URL)
# save it to disk
# we use 'wb' because these are BYTES
with open(DATA_ZIP_PATH, 'wb') as f:
    f.write(resp.content)



