# Goal: Master zero-based indexing and slicing ranges.
# Scenario: You have a list of temperature readings recorded every hour, and you need to extract specific timeframes
 
# Creating a list named temperatures
temperatures= [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

# Print the first reading (index 0) and the last reading (index -1).
print(temperatures[0:-1])

# Extracting the "Afternoon Peak" readings (the 4th, 5th, and 6th items) using slicing [3:6].
temperatures[3:6]

# Extract the "Last 3 Hours" using negative slicing [-3:].
temperatures[-3:]

# Printing all the extracted subsets with clear labels.
print("Printing the \"Afternoon Peak readings (the 4th, 5th, and 6th items)",temperatures[3:6])
print("Printing  the \"Last 3 Hours" ,temperatures[-3:])