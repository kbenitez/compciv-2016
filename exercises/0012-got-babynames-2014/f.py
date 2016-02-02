import string
import os

f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')
alphadict = {}
for line in f:
    n, s, babies = line.strip().split(',')
    last_letter = n[-1]
    if alphadict.get(last_letter):
        alphadict[last_letter] += int(babies)
    else:
        alphadict[last_letter] = int(babies)

for letter in string.ascii_lowercase:
	print(letter + ":", alphadict[letter])
f.close()



