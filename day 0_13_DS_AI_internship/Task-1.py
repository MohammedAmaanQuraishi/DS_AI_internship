#Task-1
#Goal: Understand the "shape" and characteristics of individual variables.
#Scenario: You have a dataset of housing prices. 
#          You need to know if the prices are normally distributed or skewed

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Housing.csv")
print(df)

plt.figure()
sns.histplot(df["price"], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

sns.countplot(x="area", data=df)

skewness = df["price"].skew()
kurtosis = df["price"].kurt()

print("\nSkewness of Price:", skewness)
print("Kurtosis of Price:", kurtosis)


