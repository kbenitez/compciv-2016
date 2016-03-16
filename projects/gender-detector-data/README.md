# Real Life Gender Detector Project

# About the dataset

This dataset is a listing of all current City of Chicago employees (updated March 10, 2016), complete with full names, departments, positions, and annual salaries. For hourly employees the annual salary is estimated. Human Resources owns the data, and they update the information quarterly.


## Basic facts about the dataset

- The source of the data: [City of Chicago Data Portal](https://data.cityofchicago.org)
- The data's landing page: [Current Employee Names, Salaries, and Position Titles](https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/xzkq-xp2w)
- Direct link to the data: [https://data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv?accessType=DOWNLOAD](https://data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv?accessType=DOWNLOAD)
- The data format: CSV
- Number of rows: 32062

## Description of data fields

#### Name

Contains a __text string__ representing the name of the employee.


#### Position Title

Contains a __text string__ representing the position the employee holds.


#### Department

Contains a __text string__ representing department of the employee.


#### Employee Annual Salary

Contains a __text string__ that represents the amount of money the employee receives annually. For hourly employees the annual salary is estimated. The string starts with a "$" and continues with a number that has no commas. Examples include "$90744.00" or "$2756.00".



## Anticipated data wrangling

Luckily the data is very very clean but I might rearrage the names or ensure that no middle names are listed.