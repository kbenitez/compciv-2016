from os.path import join
import json

DATA_DIR = 'tempdata'
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
wrangledFile = open(WRANGLED_JSON_FILENAME, 'r')
txt = wrangledFile.read()
wrangledFile.close()

mydict = json.loads(txt)

def detect_gender(name):
	for row in mydict:
		if (row["name"]).lower() == name.lower():
			return row
	return { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0}	
