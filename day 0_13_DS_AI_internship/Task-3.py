#TASK 3
#Goal: Understand the "shape" and characteristics of individual variables.
#Scenario: You have a dataset of housing prices. You need to know if the prices are normally distributed or skewed.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Housing.csv")
print(df)

plt.subplot(1,2,1)
corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
print("There are no two variables with correlation score higher than 0.8")
sns.heatmap(corr_matrix,annot=True)
plt.show()
plt.subplot(1,2,2)
sns.boxplot(x=df ['price'])
plt.xlabel('Price')
plt.show()
plt.tight_layout()
