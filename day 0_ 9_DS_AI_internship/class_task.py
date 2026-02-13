#Class Task-1
import pandas as pd
marks=pd.Series([100,90,80], index=["math","science","social"])
print(marks)



#Class Task-2
import pandas as pd
marks=pd.Series([100,90,80], index=["math","science","social"])
print(marks[100])
print(marks[["math","science"]])
print(marks["social"])


#Class Task-3
import pandas as pd
num=pd.Series([0,20,30,40,50,60,70,80,90,100])
print(num[num<100])


#Class Task-4
import pandas as pd
import numpy as np
num=pd.Series([0,None,30,np.nan,50,60,70,80,90,100])
print(num.isnull())
print(num.fillna(9999))

# Class Task-5
name=pd.Series(["amaan","Asif","BaBA","RAju"])
print(name.str.contains('a'))

#lowering the name
low=name.str.lower()
print(low)
print(low.str.contains('a'))
