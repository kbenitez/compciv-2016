import os

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')
NewRecordList = []
for line in f:
    name, sex, numBabies = line.strip().split(',')
    r = [name, sex, int(numBabies)]
    NewRecordList.append(r)

def popular(babyRow):
	return int(babyRow[2])

sortedBabyNames = sorted(NewRecordList, key = popular, reverse=True)[0:10]

for i in range(10):
	print (str(i+1) + ".", sortedBabyNames[i][0] + "," + sortedBabyNames[i][1] + "," + str(sortedBabyNames[i][2]))

f.close()