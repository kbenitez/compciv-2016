# Real Life Gender Detector Project

## Introduction

This dataset is a listing of all current City of Chicago employees (updated March 10, 2016), complete with full names, departments, positions, and annual salaries. For hourly employees the annual salary is estimated. Human Resources owns the data, and they update the information quarterly.
I am interested to see the gender breakdown by certain job type, and the gender breakdown by annual salary. I imagine there to be more men in politics, first responder positions, and logistics work. I also expect more women to be in health care positions or desk jobs. As for the gender breakdown by annual salary, I believe that women will be making less than men on average - so they will occupy the majority of lower paying positions.
My hypotheses for the most part came out to be true. The one surprising piece of data to me was that the highest paid person was a female. She made nearly $85,000 more than the next person on the list. I feel like if I took averages on annual salary she would be an outlier - but that's amazing for her!


## Methodology and Caveats

- The source of the data: [City of Chicago Data Portal](https://data.cityofchicago.org)
- The data's landing page: [Current Employee Names, Salaries, and Position Titles](https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/xzkq-xp2w)
- Direct link to the data: [https://data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv?accessType=DOWNLOAD](https://data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv?accessType=DOWNLOAD)
- The data format: CSV
- Number of rows: 32062

### Description of data fields

#### Name

Contains a __text string__ representing the name of the employee. Typically written as three "words", 'Last_Name, First_Name Optional_Middle_Initial'.


#### Position Title

Contains a __text string__ representing the position the employee holds.


#### Department

Contains a __text string__ representing department of the employee.


#### Employee Annual Salary

Contains a __text string__ that represents the amount of money the employee receives annually. For hourly employees the annual salary is estimated. The string starts with a "$" and continues with a number that has no commas. Examples include "$90744.00" or "$2756.00".



### Anticipated data wrangling

Luckily the data was very very clean but I: split up the first and last names into two different features; took away any quotations; removed the dollar signs in the salary fields; and made the salary strings into floats.

### Gender Classifying

To classify each employee by gender I compared the number of male babies born with the name versus female babies born (from Social Security Administration Files 1950-2014 by decade) to determine the “likely” gender of the name. If the name never was given to a baby born in the US in that time frame then the gender is classified as "NA". There simply was not enough prior data to assume gender at that point. Anyways, given the Name text string, I initially split that by comma into a "Firstish Name" (because it may or may not have included a middle initial) and a "Last Name". Then I split the "Firstish Name" string by a space and took whatever name was before the space (either leaving the middle initial behind or taking the first name that was there all along). I then used that first name to retreive the data structure that held the aforementioned ratio of male babies born versus female babies born to see what was the likely gender.

### Technical Problems

Dealing with commas within a CSV file was the biggest problem. Yes, commas are inherent to CSVs, but having the name as "Last name, First" was a huge problem when I wanted to split the row. I learned to just make more parameters/headers than I initially had wanted - but ideally there would've been a way to say "split on the ',' but not the first ','".

## Past Research and Articles

-[HIMSS survey: Men make 25% more than women in health IT](http://www.federaltimes.com/story/government/management/hr/health/2016/03/02/himss-survey-finds-men-make-25-percent-more-than-women-healthcare/81198036/)
-[Breaking the mold: Women firefighters](http://fox21news.com/2016/02/19/breaking-the-mold-women-fire-fighters/)
-[U.S. Push for Fair Pay Racks Up Few Victories](http://www.wsj.com/articles/u-s-push-for-fair-pay-racks-up-few-victories-1458065433)
-[The Wage Gap: Which Jobs Are Paying Women Less?](http://www.forbes.com/sites/shreyaagarwal/2016/03/08/the-wage-gap-which-jobs-are-paying-women-less/#b2558be5998e)
-[Government workforce is closing the gender pay gap, but reforms still needed, report says](https://www.washingtonpost.com/politics/government-workforce-is-closing-the-gender-pay-gap-but-reforms-still-needed-report-says/2014/04/13/59281484-c1b2-11e3-b574-f8748871856a_story.html)


## How To Use It

Here is the order in which I created my files and descriptions of what each file does. Anything not listed here would be created through the use of these files. 

__fetch_data.py__ - Running this script will download a csv file from the City of Chicago data portal website and store the csv file in tempdata/ as "chicago_employees.csv"

__wrangle_data.py__ - Running this script will create a new "wrangled" csv file (called "wrangled_data.csv") that contains these attributes:'Last Name', 'Firstish Name', 'Position Title', 'Department' , 'Employee Annual Salary'. It removes unwanted quotation marks and dollar signs from the data as well.

__fetch_gender_data.py__ - Running this script will download a large zip file ("names.zip") of all of the baby names data from the Social Security Administration, and it will unpack that zip file as well putting numerous txt files in tempdata/ that look like "yob(year).txt".

__wrangle_gender_data.py__ - Running this script aggregates a number of data files from 1950 to 2014, then reshapes it into a csv file and a json file ("wrangledbabynames.csv/json") for use in a gender-detecting program. By reshape I mean it creates the headers: year; name; gender; ratio; females; males; and total and fills those with the respective data points. It then sorts those rows in descending order of the total baby count and as a tiebreaker, in ascending alphabetical order of the name.
 
__gender.py__ - Running this script takes care of loading the wrangled babynames data from the easily accessible json file, "wrangledbabynames.json", and provides a reference to the detect_gender() function. 

__classify.py__ - Running this script opens and reads "wrangled_data.csv" to classify the gender of each row of the file with the detect_gender() function. It then adds the gender, ratio, and usable_name (i.e. the first name used for the detect_gender() function) attributes to the data row, which are written to a new file, "classified_data.csv".

__analyze.py__ - Running this script opens and reads "classified_data.csv" to draw interesting gender related figures from it. So it counts and divides a bunch of figures and prints statistics on gender breakdowns in the Chicago workforce.

## Analysis

### Interesting Data I Found:

#### Overall Gender Breakdown:

Here are the numbers of unique names by gender in this Chicago employee list:
F:   2059 M:   1817 NA:   1215
And here is the female to male ratio for that unique set:
F/M baby ratio: 113
So there are 1.13 times more female than male employees (unidentified gendered names aside).

This seems accurate because the split of the population is 50/50 due to chance statistics. I am upset with the large amount of unidentified genders, but that's just a testament to the amount of diversity in Chicago. The names are unique to outside the US and therefore not on our SS baby names lists and cannot be accurately classified.
 
#### Gender Breakdown by Occupation:

The amount of employees working as first responders to fire or crime is 16888.
20% of those are female.
I.E. There are 3396 female first responders to fire/ crime, and 13492 male first responders to fire/ crime.
Clearly, most first responders are male as I expected.

The amount of employees working in health or family & support services is 1090.
77% of those are female.
I.E. There are 839 female health and family supporters, and 251 male health and family supporters.
Clearly, most health and family support workers are female as I expected.

#### Gender Breakdown in the Top Tier of Incomes:
 
The highest reported income is for the job position, commissioner of aviation. The gender of the highest paying position is Female. It pays $300,000.00 per year.
Only 20% of the top 10 highest paid listed Chicago employees are female.

I actually expected the percentage to be lower. I'm super surprised by these findings and proud of those women for making it that far - but it's difficult to be on par with men wage-wise.

#### Gender Breakdown by Income Bracket:
 
Here's the proportion of females in each of the following income brackets:
$0 <= $30000        :      72% of 2050 employees.
$30000 <= $50000    :      41% of 1485 employees.
$50000 <= $100000   :      27% of 22592 employees.
$100000 <= $250000  :      17% of 4679 employees.
$250000 <= $1000000 :      100% of 1 employee.

You can see women are mostly in the lower income brackets; as the income goes up, women are less represented. The last bracket seems to be an outlier, but I'm proud of her nonetheless.
