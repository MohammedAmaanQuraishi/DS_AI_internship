import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 1. Create dummy data similar to your graph
data = {'Age': [19, 25, 28, 32, 35, 38, 43]}
df = pd.DataFrame(data)

# 2. Initialize the Scaler
scaler = StandardScaler()

# 3. Fit and transform the data
# We reshape because the scaler expects a 2D array
df['Age_Scaled'] = scaler.fit_transform(df[['Age']])

# 4. Plotting the 'Before' and 'After'
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Original Age (Similar to your uploaded image)
sns.histplot(df['Age'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Original Age Histogram')
axes[0].set_xlabel('Age (Raw Years)')

# Plot 2: Scaled Age
sns.histplot(df['Age_Scaled'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Scaled Age Histogram')
axes[1].set_xlabel('Age (Standardized Units)')

plt.tight_layout()
plt.show()

# Print values to see the difference
print("Original Values:\n", df['Age'].values)
print("\nScaled Values (Mean=0, Std=1):\n", df['Age_Scaled'].values)