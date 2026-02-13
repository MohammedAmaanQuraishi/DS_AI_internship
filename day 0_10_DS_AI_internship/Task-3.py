# Task-3

import pandas as pd
data3={
       "Location":[" New York","new york","NEW YORK ","New York"]
       }
df3=pd.DataFrame(data3)
print(df3)
#before cleaning
df3.groupby("Location").size()
print(df3["Location"].unique())
#cleaning
df3["Location"]=df3["Location"].str.strip()
df3["Location"]=df3["Location"].str.title()#or you can use str.lower
#after cleaning
print(df3["Location"].unique())
df3.groupby("Location").size()