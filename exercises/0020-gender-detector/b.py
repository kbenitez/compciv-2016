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


totalsdict = {'M': 0, 'F': 0}

for fname in myfilenames:
    babyfile = open(fname, "r")
    for line in babyfile:
        name, gender, babies = line.split(',')
        # need to convert babies to a number before adding
        totalsdict[gender] += int(babies)

# Now, totalsdict contains two keys, 'M' and 'F', which both point
# to very large integers
babyfile.close()
print("F:", str(totalsdict['F']).rjust(6),
      "M:", str(totalsdict['M']).rjust(6))


f_to_m_ratio = round(100 * totalsdict['F'] / totalsdict['M'])
print("F/M baby ratio:", f_to_m_ratio)
