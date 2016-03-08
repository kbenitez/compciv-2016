from os.path import join
import csv
import json

DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
WRANGLED_HEADERS = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']

wrangledFile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(wrangledFile))

for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])

jsonfile = open(WRANGLED_JSON_FILENAME, 'w')
# then we serialize datarows into JSON, i.e.
# convert that list of dictionaries into just plaintext that is
#  formatted like the JSON spec
jsontext = json.dumps(datarows, indent=2)
# then we write it to file object
jsonfile.write(jsontext)
# and then we close that file object
jsonfile.close()
wrangledFile.close()


csvtxt = open(WRANGLED_DATA_FILENAME).read()
jsontxt = open(WRANGLED_JSON_FILENAME).read()

csvLngth = len(csvtxt)
jsonLngth = len(jsontxt)

print("CSV has", csvLngth, "characters")
print("JSON has", jsonLngth, "characters")

size_ratio = round(((jsonLngth - csvLngth) / csvLngth), 1)
print("JSON requires", size_ratio, "times more text characters than CSV")