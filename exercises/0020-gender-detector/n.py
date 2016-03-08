from os.path import join
import json
from zoofoo import detect_gender

INTRIGUING_NAMES = ["Michael", "Kelly", "Kanye", "THOR", "casey", "Arya", "ZZZblahblah"]

numMaleBabies = maleNameTally = numFemaleBabies = femaleNameTally = NAtally = 0


for n in INTRIGUING_NAMES:
	result = detect_gender(n)
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