# -*- coding: utf-8 -*-
"""LVADSUSR105_lab2_R.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eojozA2p5RuxOx_8mEYupM-LPdjnDD6p
"""

#Regression
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score,confusion_matrix,f1_score,classification_report,r2_score,mean_squared_error,mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data  = pd.read_csv("/content/drive/MyDrive/auto-mpg.csv")
df = pd.DataFrame(data)
df.info()
df

ncount  = df.isnull().sum()
print(ncount)

df.fillna(df.mean(),inplace=True)


dcount=df.duplicated().sum()
df.drop_duplicates()

plt.figure(figsize=(10,7))
sns.boxplot(data=df)
plt.show()

q1  = df.quantile(0.25)
q3  = df.quantile(0.75)
iqr = q3-q1
outlier = ((df<q1-iqr*1.5 )| (df>q3+iqr*1.5)).any(axis=1)

ndf = df[~outlier]
plt.figure(figsize=(10,7))
sns.boxplot(data=ndf)
plt.show()

encode = LabelEncoder()
ndf["car name"] = encode.fit_transform(ndf["car name"])

ndf

sns.pairplot(data=ndf)
plt.show()

x = ndf[["cylinders","displacement","weight","acceleration"]]
y = ndf["mpg"]

std = StandardScaler()
x_std = std.fit_transform(x)

x_train,x_test,y_train,y_test  = train_test_split(x_std,y,test_size=0.3,random_state=42)

model = xgb.XGBRegressor()
model.fit(x_train,y_train)

output  = model.predict(x_test)

r2score=r2_score(y_test,output)
mse  = mean_squared_error(y_test,output)
rmse  = mse **0.5
mae = mean_absolute_error(y_test,output)

print(r2score)
print(mse)
print(rmse)
print(mae)

plt.scatter(y_test,output)
plt.xlabel(["y_test"])
plt.ylabel(["output"])
plt.legend()
plt.show()