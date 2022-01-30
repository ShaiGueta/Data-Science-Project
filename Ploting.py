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


df = pd.read_csv('Players_Edited.csv')
df.drop('Unnamed: 0',axis = 1,inplace=True)
df.drop('Name',axis = 1,inplace=True)

# Matrix
# corrMatrix = df.corr()
# sn.heatmap(corrMatrix, annot=True)
# plt.show()

# Graphs
x = 'Version'
y = 'Price'
plot = plt.scatter(df[x],df[y])
plt.xlabel(x)
plt.ylabel(y+'(mil)')
plt.show()
