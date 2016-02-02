import os

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')
numBabies = 0
for x in f:
    numBabies += int((x.split(","))[2])

print("There are", numBabies ,"babies whose names were recorded in 2014.")
f.close()