# Class Task :
import numpy as np 
import pandas as pd

data ={
      
       "stud_id":[1,2,3,4,5,None],
       "name":["amaan","amaan",None,np.nan,"saqeeb","muthaheer"],
       "city":["madina",None,"   bangalore","hydrabad   ","  hydrabad",None]
       }

df = pd.DataFrame(data)
print(df)


print(df.head())

print(df.info())

print(df.isna().sum())

df["city"]=df["city"].fillna(df["city"].mode()[0])
print(df)
    
df["stud_id"]=df["stud_id"].fillna(df["stud_id"].mean())
print(df)
    
print(df.dtypes)

df["stud_id"] = df["stud_id"].astype(int)
print(df.dtypes)

df["city"] = df["city"].str.strip()

# Convert City names to lowercase
df["city"] = df["city"].str.lower()

print("\nCity column after cleaning:")
print(df["name"])
print(df.duplicated("name").sum())

print(df.drop_duplicates(subset="name"))
print(df.drop_duplicates(subset="name",keep="last"))
print(df.drop_duplicates(subset="name"))#by default first
result=print(df.drop_duplicates(subset="name",inplace= True))
print(result)
result=print(df.drop_duplicates(subset="name",inplace= False))
print(result)


#ignore_index
result=print(df.drop_duplicates(subset="name",ignore_index=True))
print(result)