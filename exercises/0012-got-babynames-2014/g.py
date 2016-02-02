import string
import os

fixed_width = 8
f = open((os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')), 'r')
genderNamedict = {'F': {}, 'M': {}}
for line in f:
    name, sex, babies = line.strip().split(',')
    last_letter = name[-1]
    if 'F' in sex:
	    if genderNamedict["F"].get(last_letter):
	        genderNamedict["F"][last_letter] += int(babies)
	    else:
	        genderNamedict["F"][last_letter] = int(babies)
    else:
	    if genderNamedict["M"].get(last_letter):
	        genderNamedict["M"][last_letter] += int(babies)
	    else:
	        genderNamedict["M"][last_letter] = int(babies)

print("letter".ljust(fixed_width) + "F".rjust(fixed_width) + "M".rjust(fixed_width))
print("-"*24)
for letter in string.ascii_lowercase:
	print(letter.ljust(fixed_width) + str(genderNamedict["F"][letter]).rjust(fixed_width) + str(genderNamedict["M"][letter]).rjust(fixed_width))
f.close()



