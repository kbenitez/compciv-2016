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


## How To Use It