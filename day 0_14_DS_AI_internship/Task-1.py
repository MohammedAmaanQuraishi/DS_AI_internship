import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.metrics import r2_score
import seaborn as sns
import matplotlib.pyplot as plt

data={
      'Name':["A","B","C","D","E","F"],
      'Transmission':['Automatic','Automatic','Manual','Manual','Manual','Automatic'],
      'Color':['Red','Blue','Red','Green','Blue','Green']
      }
df=pd.DataFrame(data)
le=LabelEncoder()
df["Transmission"]=le.fit_transform(df["Transmission"])
df= pd.get_dummies(df,columns=["Color"],drop_first=True)