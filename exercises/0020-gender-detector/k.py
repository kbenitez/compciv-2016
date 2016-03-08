from os.path import join
import csv

DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
INTRIGUING_NAMES = ["Michael", "Kelly", "Kanye", "THOR", "casey", "Arya", "ZZZblahblah"]

wrangledFile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(wrangledFile))
numMaleBabies = maleNameTally = numFemaleBabies = femaleNameTally = NAtally = 0

def showMeTheName(name, csvDict):
	numNames = len(csvDict)
	for row in range(numNames):
		if (csvDict[row]["name"]).lower() == name.lower():
			return csvDict[row]
	return { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0}		

for n in INTRIGUING_NAMES:
	result = showMeTheName(n, datarows)
	print(n, result['gender'], result['ratio'])
	if result['gender'] is "F":
		femaleNameTally += 1	
		numFemaleBabies += int(result["females"])
		numMaleBabies += int(result["males"])
	elif result['gender'] is "M":
		maleNameTally += 1
		numFemaleBabies += int(result["females"])
		numMaleBabies += int(result["males"])
	else:
		NAtally += 1

print("Total:")
print("F:", femaleNameTally, 'M:', maleNameTally, 'NA:', NAtally)
print('females:', numFemaleBabies, 'males:', numMaleBabies)