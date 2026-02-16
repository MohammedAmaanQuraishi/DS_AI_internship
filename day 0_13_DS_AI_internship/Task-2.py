#Task-2
#Goal: Discover how variables interact with one another.
#Scenario: Does a larger house size (SquareFootage) always mean a higher Price?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (if not already loaded)
df = pd.read_csv("Housing.csv")

plt.figure(figsize=(8,5))


sns.scatterplot(x="area_sqft", y="price", data=df)

plt.title("Area vs Price")
plt.xlabel("Area (Square Feet)")
plt.ylabel("Price")
plt.show()

sns.boxplot(x="city", y="price", data=df)

plt.xticks(rotation=90)
plt.title("House Price Distribution by City")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()

"""This indicates a positive relationship between area and price — larger houses generally cost more.1



✅ Why This Matters (Feature Selection)

If area_sqft strongly affects price → it is an important feature.

If some cities have consistently higher prices → city is also an important feature.

Features that show no pattern → may be less useful for ML models."""