import os

fname = os.path.join('tempdata', 'tragedies', 'hamlet')
hamletfile = open(fname, 'r')
lines = 0
for x in hamletfile:
    lines += 1
hamletfile.close()

print(fname, "has", lines, "lines")