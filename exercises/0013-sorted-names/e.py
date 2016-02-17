import os

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')

nBabies = 0
GenderFreeRecordList = {}
for line in f:
    name, sex, numBabies = line.strip().split(',')
    nBabies += int(numBabies)
    if GenderFreeRecordList.get(name):
    	GenderFreeRecordList[name] += int(numBabies)
    else:
    	GenderFreeRecordList[name] = int(numBabies)

nameList = []
names = GenderFreeRecordList.keys()
numNames = len(names)

for name in names:
	nameList.append([name, GenderFreeRecordList[name]])

def popular(babyRow):
	return (babyRow[1])

sortedBabyNames = sorted(nameList, key = popular, reverse=True)

topTenBabyAmount = topHundredBabyAmount = topThousandBabyAmount = topTenThousandBabyAmount = RestBabyAmount = 0

for i in range(numNames):
	if i < 10:
		topTenBabyAmount += sortedBabyNames[i][1]
	elif i < 100:
		topHundredBabyAmount += sortedBabyNames[i][1]
	elif i < 1000:
		topThousandBabyAmount += sortedBabyNames[i][1]
	elif i <10000:
		topTenThousandBabyAmount += sortedBabyNames[i][1]
	else:
		RestBabyAmount += sortedBabyNames[i][1]

print("Names 1 to 10:", str(round(float(topTenBabyAmount)/float(nBabies)*100, 1)))
print("Names 11 to 100:", str(round(float(topHundredBabyAmount)/float(nBabies)*100, 1)))
print("Names 101 to 1000:", str(round(float(topThousandBabyAmount)/float(nBabies)*100, 1)))
print("Names 1001 to 10000:", str(round(float(topTenThousandBabyAmount)/float(nBabies)*100, 1)))
print("Names 10001 to", str(numNames) + ":", str(round(float(RestBabyAmount)/float(nBabies)*100, 1)))
f.close()