import re
from os.path import join, basename
from glob import glob

START_YEAR = 1950
END_YEAR = 2015

DATA_DIR = 'tempdata'
pattern = "(yob19[5-9][0-9]\.txt)|(yob20[01][0-9]\.txt)"
alltxtfiles_names = glob(join(DATA_DIR, '*.txt'))

myfilenames = []
for fname in alltxtfiles_names:
    matchobj = re.search(pattern, fname, flags=0)
    if matchobj:
        myfilenames.append(fname)

for year in range(START_YEAR, END_YEAR, 5):
	babyfile = open(myfilenames[year-START_YEAR], "r")

	tally = {'M': set(), 'F': set()}
	tallyWhole = set()
	numBabies = 0
	numMBabies = 0
	numFBabies = 0
	for line in babyfile:
		name, gender, babies = line.split(',')
		numBabies += int(babies)
		tallyWhole.add(name)
		tally[gender].add(name)
		if gender is "M":
			numMBabies += int(babies)
		else:
			numFBabies += int(babies)
	babyfile.close()
	print(year)
	print("Total:", round(numBabies / len(tallyWhole)), 'babies per name')
	print("    M:", round(numMBabies / (len(tally['M']))), "babies per name")
	print("    F:", round(numFBabies / (len(tally['F']))), "babies per name")