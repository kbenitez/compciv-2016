import os

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')
numFemBabies = 0
numMaleBabies = 0
for x in f:
    name, sex, babies = (x.strip()).split(',')
    if "F" in sex:
        numFemBabies += int(babies)
    else:
        numMaleBabies += int(babies)

print("F:", numFemBabies)
print("M:", numMaleBabies)
f.close()