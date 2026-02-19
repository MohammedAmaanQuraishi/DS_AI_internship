# Task-3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Right-skewed income distribution
income = np.random.exponential(scale=50000, size=100000)

df = pd.DataFrame({"Income": income})


sample_means = []

for i in range(1000):
    sample = df["Income"].sample(n=30)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)


sample_means_df = pd.DataFrame({"Sample_Means": sample_means})


plt.figure(figsize=(8,5))
sns.histplot(sample_means_df["Sample_Means"], kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.show()
