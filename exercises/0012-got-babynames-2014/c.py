import os

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')

numDaenBabies = 0
numKhalBabies = 0

for line in f:
    if "Daenerys," in line:
        numDaenBabies += int((line.split(","))[2])
    elif "Khalees" in line:
        numKhalBabies += int((line.split(","))[2])
    elif "Khaless" in line:
        numKhalBabies += int((line.split(","))[2])

print("Daenerys:", numDaenBabies)
print("Khaleesi:", numKhalBabies)

f.close()

