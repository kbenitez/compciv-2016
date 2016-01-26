import os

hamletfile = open((os.path.join('tempdata', 'tragedies', 'hamlet')), 'r')
for x in range(5):
    print(hamletfile.readline().strip())
hamletfile.close()