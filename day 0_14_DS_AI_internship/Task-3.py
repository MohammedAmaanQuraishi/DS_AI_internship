import pandas as pd
from sklearn.preprocessing import  PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("gdp.csv")
X_train,X_test,y_train,y_test = train_test_split(df[['Year']],df[['Value']],test_size=0.2,random_state=42)


model=LinearRegression()
model.fit(X_train,y_train)
baseline_pred=model.predict(X_test)
baseline_score=r2_score(y_test, baseline_pred)

print(baseline_score)


poly=PolynomialFeatures(degree=2,include_bias=False)

X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)

poly_model=LinearRegression()
poly_model.fit(X_train_poly,y_train)
poly_pred=poly_model.predict(X_test_poly)
poly_score=r2_score(y_test, poly_pred)
print(poly_score)