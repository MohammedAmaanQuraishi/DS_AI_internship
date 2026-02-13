# Task-1

# Goal: Practice visualizing trends over continuous data
# Scenario: You are tracking the growth of a small startup's monthly revenue over five months.

# Importing the mayhplotlib  
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]
plt.plot(months,revenue) #Using plot function


# Adding the title
plt.title("Monthly Revenue Growth")

# Adding the x lable
plt.xlabel("Month")

# Adding the y lable
plt.ylabel("Revenue in USD")


# Why:
""" Line plots are essential for recognizing trends
 and slopes in ordered numerical sequences faster than reading tables."""


# Description of this graph
"""This graph shows monthly revenue growth over five months. 
Revenue increases from $2000 in Month 1 to $4500 in Month 2,
 slightly drops to $4000 in Month 3, then rises sharply to $7500 in Month 4 
 and reaches a peak of $9000 in Month 5. Overall, the trend shows steady growth
 with a small dip in the middle."""
