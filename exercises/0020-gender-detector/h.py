from os.path import join, basename
from glob import glob
import csv

DATA_DIR = 'tempdata'

WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')

wrangledFile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(wrangledFile))


print("Most popular names with <= 60% gender skew:")

firstxrows = [r for r in datarows if int(r['ratio']) <= 60 ]

for row in firstxrows[0:5]:
    print(row['name'].ljust(10), row['gender'], row['ratio'], row['total'])


wrangledFile.close()