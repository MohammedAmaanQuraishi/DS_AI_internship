# Task-1
#Goal: Practice creating a Series with custom labels and accessing specific data.
#Scenario: You are managing a small electronics store.

# Importing pandas
import pandas as pd

# Creating a Pandas Series named products
products =pd.Series([700, 150, 300],index=['Laptop', 'Mouse', 'Keyboard'])

# Printing the panda series
print( products )

# Accessing the price of 'Laptop'
print("The price of the device is", products ['Laptop'])

# Slice the Series to show the first two products using positional indexing.
print( products.iloc[0:2])

