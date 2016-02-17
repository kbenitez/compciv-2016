import os

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')
FemXNames = []
MalXNames =[]
for line in f:
    name, sex, numBabies = line.strip().split(',')
    if "x" in name or "X" in name:
    	r = [name, sex, int(numBabies)]
    	if "F" in sex:
    		FemXNames.append(r)
    	else:
    		MalXNames.append(r)

def popular(babyRow):
	return int(babyRow[2])

popFemXNames = sorted(FemXNames, key = popular, reverse=True)[0:5]
popMalXNames = sorted(MalXNames, key = popular, reverse=True)[0:5]

print("Female")
for i in range(5):
	print (str(i+1) + ". " + popFemXNames[i][0].ljust(11) + str(popFemXNames[i][2]).rjust(11))
print("Male")
for i in range(5):
	print (str(i+1) + ". " + popMalXNames[i][0].ljust(11) + str(popMalXNames[i][2]).rjust(11))

f.close()



