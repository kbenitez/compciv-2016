import os

numLinesToRead = 5

fname = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
rAndJfile = open(fname, 'r')
lines = 0
for x in rAndJfile:
    lines += 1
rAndJfile.close()

fname = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
rAndJfile = open(fname, 'r')
startLine = lines - numLinesToRead 
endLine = lines + 1
for n in range(startLine): 
    rAndJfile.readline()
for x in range(startLine+1, endLine):
    print(str(x) + ":", rAndJfile.readline().strip())
rAndJfile.close()


