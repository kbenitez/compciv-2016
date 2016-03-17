from os.path import join
from csv import DictReader, DictWriter
DATA_DIR = 'tempdata'
thefilename = join(DATA_DIR, 'chicago_employees.csv')

WRANGLED_HEADERS = ['Last Name', 'Firstish Name', 'Position Title', 'Department' , 'Employee Annual Salary']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled_data.csv')

dicList = []
with open(thefilename, 'r') as thefile:
    #skip the headline line
    thefile.readline()
    for line in thefile:
        try:
        	lastName, firstishName, position, dept, salary = line.split(",")
	        xdict = {}
	        xdict['Last Name'] = lastName[1:] #ignore the first quotation mark
	        xdict['Firstish Name'] = firstishName[2:-1] #ignore the last quotation mark
	        xdict['Position Title'] = position
	        xdict['Department'] = dept
	        xdict['Employee Annual Salary'] = float(salary[1:])
	        dicList.append(xdict)
        except ValueError:
	        pass



thefile.close()

wfile = open(WRANGLED_DATA_FILENAME, 'w')
# turn it into a DictWriter object, and tell it what the fieldnames are
wcsv = DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
# write the headers row
wcsv.writeheader()

def moneyThenNameRank(xdict):
    # and return a tuple of negative salary, and first name
    return (-xdict['Employee Annual Salary'], xdict['Firstish Name'])

my_final_list = sorted(dicList, key=moneyThenNameRank)
for row in my_final_list:
    wcsv.writerow(row)
# the end...close the file
wfile.close()
