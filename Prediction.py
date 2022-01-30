from numpy import NaN, nan
from numpy.lib.twodim_base import tri
import pandas as pd
from pandas import DataFrame
from typing import Text
from bs4 import BeautifulSoup
from bs4.element import ProcessingInstruction
from pandas.core.algorithms import unique
import requests
import seaborn as sn
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('Players_Edited.csv')
df = df[df['Price']<4000000]
df = df[df['Price']>900]
df.drop('Unnamed: 0',axis = 1,inplace=True)
df.drop('Name',axis = 1,inplace=True)
#df.drop('Work_Rates',axis = 1,inplace=True) - Hardly makes a diffrance
#df.drop('Strong_Foot',axis = 1,inplace=True) - Hardly makes a diffrance
#df.drop('Position',axis = 1,inplace=True) - Makes a 1% diffrance
df.drop('Nation',axis = 1,inplace=True)

NoPriceList = df.columns[df.columns != 'Price']
OnlyPriceList = 'Price'
X = df[NoPriceList]
Y = df[OnlyPriceList]

x_train, x_test, y_train, y_test = train_test_split(X, Y,random_state=0,test_size=0.3)
i = int(1)

#parameters = {'n_estimators':[300,350]}

model = RandomForestRegressor(random_state=0,max_depth=20,n_estimators=150)
# cv = GridSearchCV(model, parameters,scoring='r2')
# cv.fit(x_train,y_train)
# print(cv.best_params_,cv.best_score_)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print(r2_score(y_test,y_pred))


