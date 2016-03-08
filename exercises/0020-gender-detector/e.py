from os.path import join, basename
from glob import glob

DATA_DIR = 'tempdata'
alltxtfiles_names = glob(join(DATA_DIR, '*.txt'))
numTxtFiles = len(alltxtfiles_names)

file14 = alltxtfiles_names[numTxtFiles-1]

totalsdict = {'M': 0, 'F': 0}
tally = {'M': set(), 'F': set()}
tallyWhole = set()
babyfile = open(file14, "r")
for line in babyfile:
	name, gender, babies = line.split(',')
	tallyWhole.add(name)
	tally[gender].add(name)
	totalsdict[gender] += int(babies)
babyfile.close()
print("Total:", str(len(tallyWhole)), "unique names for", str(totalsdict['F'] + totalsdict['M']), "babies")
print("    M:", str(len(tally['M'])), "unique names for", str(totalsdict['M']), "babies")
print("    F:", str(len(tally['F'])), "unique names for", str(totalsdict['F']), "babies")