from os.path import join, basename
from glob import glob
import csv

DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')
GENDER_RATIOS = [60, 70, 80, 90, 99]
TOTAL_BABY_LIMIT = 100

wrangledFile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(wrangledFile))


print("Popular names in 2014 with gender ratio less than or equal to:")

for ratio in GENDER_RATIOS:
	ratioRows = [r for r in datarows if ((int(r['ratio']) <= ratio) and (int(r["total"]) >= TOTAL_BABY_LIMIT)) ]
	over100Rows = [row for row in datarows if int(row["total"]) >= TOTAL_BABY_LIMIT ]
	print("  " + str(ratio) + "%:", str(len(ratioRows)) + "/" + str(len(over100Rows)))


wrangledFile.close()