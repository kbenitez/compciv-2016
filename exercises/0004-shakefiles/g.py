import os
import glob

numLinesToRead = 5

tragic_path = os.path.join('tempdata', 'tragedies', '*')
shakeTrags = glob.glob(tragic_path)

for tragedy in shakeTrags:
	fname = os.path.join(tragedy)
	filename = open(fname, 'r')
	lines = 0
	for x in filename:
	    lines += 1
	filename.close()
	print(fname, "has", lines, "lines")

	fname = os.path.join(tragedy)
	filename = open(fname, 'r')
	startLine = lines - numLinesToRead 
	endLine = lines + 1
	for n in range(startLine): 
	    filename.readline()
	for x in range(startLine+1, endLine):
	    print(str(x) + ":", filename.readline().strip())
	filename.close()