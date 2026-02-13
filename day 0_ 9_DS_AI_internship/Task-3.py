# Task-3
#Goal: Process text data efficiently using the .str accessor.

#Scenario: A list of usernames was collected with inconsistent casing and extra spaces

# Importing pandas
import pandas as pd

#Create a Series named usernames
usernames=pd.Series( [' Alice', 'bOB', 'Charlie_Data ', 'daisy'])

# Removing leading/trailing whitespace (.strip())
remove=usernames.str.strip()

# Converting all names to lowercase (.lower()).
low=usernames.str.lower()

# Checking which names contain the letter 'a' (.contains()).
contains=low.str.contains('a')

#displaying Cleaned Series
print("Cleaned Series",remove)

#displaying boolean result
print("The boolean result of the 'a' search.",contains)
