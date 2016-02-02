import os

#calculated in a.py
numLinesInFile = 33044

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')
print("Top baby girl names")
for x in range(5):
    name, sex, babies = (f.readline().strip()).split(',')
    print(str(x+1) + ".", name, babies)

print("")
print("Top baby boy names")
boyN = 1
for x in range(5, numLinesInFile):
    name, sex, babies = (f.readline().strip()).split(',')
    if "M" in sex and boyN < 6:
        print(str(boyN) + ".", name, babies)
        boyN += 1

f.close()