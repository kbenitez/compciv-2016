import re
from os.path import join, basename
from glob import glob

DATA_DIR = 'tempdata'
pattern = "(yob19[5-9][0-9]\.txt)|(yob20[01][0-9]\.txt)"
alltxtfiles_names = glob(join(DATA_DIR, '*.txt'))

myfilenames = []
for fname in alltxtfiles_names:
    matchobj = re.search(pattern, fname, flags=0)
    if matchobj:
        myfilenames.append(fname)


tally = {'M': set(), 'F': set()}

for fname in myfilenames:
    babyfile = open(fname, "r")
    for line in babyfile:
        name, gender, babies = line.split(',')
        tally[gender].add(name)
    babyfile.close()
# Now, tally contains two keys, 'M' and 'F', which both point
# to a set of names

print("F:", str(len(tally['F'])).rjust(6),
      "M:", str(len(tally['M'])).rjust(6))


f_to_m_ratio = round(100 * len(tally['F']) / len(tally['M']))
print("F/M baby ratio:", f_to_m_ratio)