#Task 2
import pandas as pd
import numpy as np

data = {
    "student_id": [1, 2, 3, 4, 5, 6],
    "name": ["asif", "amaan", None, np.nan, "amaan", "pig"],
    "city": ["bangalore", "gulbarga", None, np.nan, "wadi", "shabad"],
    "Price": ["$100", "$250", "$175", "$300", "$400", "$150"],
    "Date": ["2024-01-01", "2024-02-15", "2024-03-10", "2024-04-05", "2024-05-12", "2024-06-20"]
}

df = pd.DataFrame(data)

print("Initial Data Types:")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nData Types After Conversion:")
print(df.dtypes)

print("\nUpdated DataFrame:")
print(df)