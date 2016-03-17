from os.path import join
import csv

DATA_DIR = 'tempdata'
CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified_data.csv')
TOP_ROWS_LENGTH = 10
INCOME_VALUES = [0, 30000, 50000, 100000, 250000, 1000000]

classifiedFile = open(CLASSIFIED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(classifiedFile))
genderedrows = [r for r in datarows if r['Gender'] != 'NA']

#####################################################################

print(" ")

tally = {'M': set(), 'F': set(), 'NA': set()}

for employee in datarows:
    gender = employee['Gender']
    tally[gender].add(employee['Usable Name'])

# Now, tally contains two keys, 'M' and 'F', which both point
# to a set of names

print("Here are the numbers of unique names by gender in this Chicago employee list:")
print("F:", str(len(tally['F'])).rjust(6),
      "M:", str(len(tally['M'])).rjust(6),
      "NA:", str(len(tally['NA'])).rjust(6))

print("And here is the female to male ratio for that unique set:")
percentage = len(tally['F']) / len(tally['M'])
f_to_m_ratio = round(100 * percentage)
print("F/M baby ratio:", f_to_m_ratio)
print("So there are", round(percentage, 2), "times more female than male employees (unidentified gendered names aside).")

#####################################################################

print(" ")

emergencyRespRows = [r for r in genderedrows if 'FIRE' in r['Department'] or 'POLICE' in r['Department']]
print("The amount of employees working as first responders to fire or crime:", len(emergencyRespRows))
femaleemergencyRespRows = [r for r in emergencyRespRows if r['Gender'] == 'F']
maleemergencyRespRows = [r for r in emergencyRespRows if r['Gender'] == 'M']
print( round(100 * (len(femaleemergencyRespRows) / len(emergencyRespRows))), "percent of those are female.")
print("I.E. There are", len(femaleemergencyRespRows), "female first responders to fire/ crime, and", len(maleemergencyRespRows), "male first responders to fire/ crime.")

familyAndHealthrows = [r for r in genderedrows if 'FAMILY & SUPPORT' in r['Department'] or 'HEALTH' in r['Department']]
print("The amount of employees working in health or family & support services:", len(familyAndHealthrows))
femalefamilyAndHealthrows = [r for r in familyAndHealthrows if r['Gender'] == 'F']
malefamilyAndHealthrows = [r for r in familyAndHealthrows if r['Gender'] == 'M']
print( round(100 * (len(femalefamilyAndHealthrows) / len(familyAndHealthrows))), "percent of those are female.")
print("I.E. There are", len(femalefamilyAndHealthrows), "female health and family supporters, and", len(malefamilyAndHealthrows), "male health and family supporters.")

#####################################################################

print(" ")
highestPaid = datarows[0]
print("The highest reported income is for the job position,", 
	(highestPaid['Position Title']).lower() + ". The gender of the highest paying position is", 
	highestPaid['Gender'] + ". It pays $", highestPaid['Employee Annual Salary'], "per year.")
topTenRows = datarows[:TOP_ROWS_LENGTH]
femBigBuckRows = [r for r in topTenRows if r['Gender'] == 'F']
proportion = round(100 * (len(femBigBuckRows) / TOP_ROWS_LENGTH))
if proportion < 40:
	print("Only", proportion, "percent of the top", TOP_ROWS_LENGTH, "highest paid listed Chicago employees are female.")
else:
	print(proportion, "percent of the top", TOP_ROWS_LENGTH, "highest paid listed Chicago employees are female.")

#####################################################################

print(" ")
print("Here's the proportion of females in each of the following income brackets:")
numLevels = len(INCOME_VALUES)
for level in range(numLevels-1):
	IncomeRows = [r for r in genderedrows if float(r['Employee Annual Salary']) >= INCOME_VALUES[level] and float(r['Employee Annual Salary']) < INCOME_VALUES[level+1]]
	fems = [r for r in IncomeRows if r['Gender'] == 'F']
	numEmployees = len(IncomeRows)
	print("$" + str(INCOME_VALUES[level]), "<=", "$" + str(INCOME_VALUES[level+1]), ":     ", str(round(100 * (len(fems) / numEmployees))) + "% of", numEmployees, "employee(s).")

classifiedFile.close()
