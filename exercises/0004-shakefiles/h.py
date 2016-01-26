from os.path import join
from glob import glob

pattern = join('tempdata', '**', '*')
filenames = glob(pattern) 

totalNumLines = 0
totalnonBlankLines = 0
for f in filenames:
	fname = join(f)
	shakefile = open(fname, 'r')
	nonblankLines = 0
	totalLines = 0
	for line in shakefile:
	    totalLines += 1
	    if line.strip() != "":
	    	nonblankLines += 1
	shakefile.close()
	totalnonBlankLines += nonblankLines
	totalNumLines += totalLines
	print(fname, "has", nonblankLines, "non-blank lines out of", totalLines, "total lines")

print("All together, Shakespeare's",len(filenames), "text files have:")
print(totalnonBlankLines, "non-blank lines out of", totalNumLines, "total lines")
