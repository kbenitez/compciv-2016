from os.path import join
import json
from gender import detect_gender
from csv import DictReader, DictWriter

DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled_data.csv')
WRANGLED_HEADERS = ['Last Name', 'Firstish Name', 'Position Title', 'Department' , 'Employee Annual Salary', 'Gender', 'Ratio', 'Usable Name']
CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified_data.csv')

wrangledFile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(DictReader(wrangledFile))

def extract_usable_name(firstishName):
    return firstishName.split(' ')[0]

dicList = []
for employee in datarows:
    usable_name = extract_usable_name(employee['Firstish Name'])
    result = detect_gender(usable_name)
    employee['Gender'] = result['gender']
    employee['Ratio'] = result['ratio']
    employee['Usable Name'] = usable_name
    employee['Employee Annual Salary'] = float(employee['Employee Annual Salary'])
    dicList.append(employee)

wrangledFile.close()


wfile = open(CLASSIFIED_DATA_FILENAME, 'w')
# turn it into a DictWriter object, and tell it what the fieldnames are
wcsv = DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
# write the headers row
wcsv.writeheader()

def moneyThenNameRank(xdict):
    # and return a tuple of negative salary, and first name
    return (-xdict['Employee Annual Salary'], xdict['Usable Name'])

my_final_list = sorted(dicList, key=moneyThenNameRank)
for row in my_final_list:
    wcsv.writerow(row)
# the end...close the file
wfile.close()