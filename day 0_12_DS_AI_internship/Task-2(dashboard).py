# Task-2
# Goal: Build categorical comparisons and arrange multiple plots using subplots.

# Scenario: Compare sales across three different product categories and display it alongside a trend line.


import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)

categories =['Electronics', 'Clothing', 'Home' ]
values = [300, 450, 200]
plt.bar(categories,values)

plt.subplot(1, 2, 2)
plt.plot([1,2,3,4,5],[1,2,3,4,5])

plt.tight_layout()
plt.show()