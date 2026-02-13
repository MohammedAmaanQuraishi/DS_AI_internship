# Task-2
# Goal: Use boolean masking to filter data and handle incomplete records.
# Scenario: You have a list of student exam scores, but some students missed the test.


# Importing pandas
import pandas as pd

#Creating a Series named grades
grades=pd.Series( [85, None, 92, 45, None, 78, 55])

#Printing the original list
print(grades)

#Identifing which values are missing using.isnull().
null_values=grades.isnull()
print("viewing null values",null_values)

#Fill the missing values with a default score of O using .fillna().
filled_series=grades.fillna(0)
print("viewing missing values",filled_series)

#Applying a boolean mask to filter 
filtered_result=grades[grades<60]
print("viewing after filtering values",filtered_result)
