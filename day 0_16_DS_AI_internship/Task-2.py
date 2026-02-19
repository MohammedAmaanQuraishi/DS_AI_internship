# Task-2 
import numpy as np
import pandas as pd

np.random.seed(42)

# Normal dataset (example: exam scores)
data = np.random.normal(loc=70, scale=10, size=1000)

df = pd.DataFrame({"Scores": data})

mu = df["Scores"].mean()
sigma = df["Scores"].std()

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)

df["z_score"] = (df["Scores"] - mu) / sigma

print(df.head())

outliers = df[abs(df["z_score"]) > 3]

print("Number of Outliers:", len(outliers))
print(outliers)
