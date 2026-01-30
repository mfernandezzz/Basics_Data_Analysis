#Data Analysis process:
#1) Data extraction: SQL, Scrapping, file formats (csv, json, xml), consulting APIs, distributed databases, buying data.
#2) Data cleaning: Missing values and empty data, Data imputation, Incorrect types, Incorrect or invalid values, Outliers and non relevant data, Statistical sanitization.
#3) Data wrangling: Hierarchical data, Handling categorical data, Reshaping and transforming structures, Indexing data for quick access, Merging combining and joining data.
#4) Analysis: Exploration, Building statistical models, Visualizations and representation, Correlation vs causation analysis, Hypothesis testing, Statistical analysis, reporting.
#5) Building machine learning models, feature engineering, moving ML into production, Live dashboard and reporting, Decision making and real-life tests.

#What does the shape of our dataframe tell us?
#How many rows and columns our dataframe has.

#What does the loc method allow you to do?
#Access a group of rows and columns by suppling label(s) arguments.

#What are the three main types of Jupyter notebooks cell?
#Code, Markdown and raw

#What kind of data can you import and work with in a Jupyter Notebook?
#Excel files, CSV files, XML files, Data from an API.

#Why is Numpy an important, but unpopular Python library?
#Often you wont work directly with NumPy.

#About how much memory does the integer 5 consume in plain Python?
#20 bytes.

import numpy as np
import pandas as pd
import matplotlib as plt
import csv

#What will the following code print out?
a = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'], 
    ['g', 'h', 'i']
])
print(a[:, :2]) #The first two elements of each array (or row).

#What will the following code print out?
a = np.arange(5)
print(a <= 3) #True True True True False

#What is the relationship between size of objects (such as lists and datatypes) in memory in Python's standard library and the NumPy library? Knowing this, what are the implications for performance?
#Standard Python objects take up more memory than NumPy objects; operations on NumPy objects complete very quickly compared to comparable objects in standard Python.

#What will the following code print out?
certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index = ['Tom', 'Kris', 'Ahmad', 'Beau']
)
print(certificates_earned) #Tom 8 Kris 2 Ahmad 5 Beau 6 dtype: int64

#What will the following code print out?
print(certificates_earned[certificates_earned > 5]) #Tom 8 Beau 6

#What will the following code print out?
certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})
certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']
print(certificates_earned.iloc[2]) #Certificates 5 Time (in months) 9

#What will the following code print out?
names = ['Tom', 'Kris', 'Ahmad', 'Beau']
certificates_earned.index = names
longest_streak = pd.Series([13, 11, 9, 7], index = names)
certificates_earned['Longest streak'] = longest_streak
print(certificates_earned)

#Creation of a column in a dataframe:
certificates_earned['Certificates per month'] = round(
    certificates_earned['Certificates'] / certificates_earned['Time (in months)'], 2
)
print(certificates_earned)

#What will the following code print out?
s = pd.Series(['a', 3, np.nan, 1, np.nan])
print(s.notnull().sum())

#What will the following code print out?
s = pd.Series([np.nan, 1, 2, np.nan, 3])
s = s.fillna(s.mean())
print(s) #fill nan values with the mean value of the list

#When using Matplotlib's global API, what does the order of numbers mean here?
plt.sublpot(1, 2, 1) #My figure will have one row, two columns, and i am going to start drawing in the first (left) plot.

#Fill in the blanks for the missing arguments below:
with open('certificates.csv', 'r') as fp: #name of the csv file
    reader = csv.reader(fp, delimiter='$') #specify the delimiter between the data in the rows
    next(reader)
    for index, values in enumerate(reader):
        name, certs_num, months_num = values
        print(f"{name} earned {certs_num} certificates in {months_num} months") #final string

#How would you import the csv file data.csv and store it in a DataFrame using the pandas module?
df = pd.read_csv('data.csv')

#What method does a Cursor instance have and what does it allow?
#The Cursor instance has an .execute() method wich will receive SQL parameters to run against the database.