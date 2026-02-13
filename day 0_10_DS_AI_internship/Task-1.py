#Task 1
# Goal: Detect and handle the two most common data quality issues.

# Scenario: You have received a customer_orders.csv file with several missing order IDs and repeated entries from a system glitch.

# Task 1
# Goal: Detect and handle the two most common data quality issues.

import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")


#  Print original shape

print("Original Shape:", df.shape)

#  Missing value report
print("\nMissing Values Report:")
print(df.isna().sum())


# Fill numeric missing values with median

numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())


#  Remove duplicate rows

duplicates = df.duplicated().sum()
print("\nNumber of Duplicate Rows:", duplicates)

df = df.drop_duplicates()

#  Print cleaned shape

print("\nCleaned Shape:", df.shape)
