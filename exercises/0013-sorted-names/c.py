import os

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')
nameNumDict = {}
for line in f:
        name, sex, babies = line.strip().split(',')
        if nameNumDict.get(name):
            nameNumDict[name] += int(babies)
        else:
            nameNumDict[name] = int(babies)
filteredList = []
names = nameNumDict.keys()
for name in names:
	if nameNumDict[name] >= 2000:
		filteredList.append([name, nameNumDict[name]])

def longest(nameEntry):
	return (len(nameEntry[0]), nameEntry[1])

sortedBabyNames = sorted(filteredList, key = longest, reverse=True)[0:10]

for item in sortedBabyNames:
	print(item[0].ljust(12) + str(item[1]).rjust(12))
	
f.close()


