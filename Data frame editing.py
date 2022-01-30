from numpy import NaN, nan
from numpy.lib.twodim_base import tri
import pandas as pd
from pandas import DataFrame
from typing import Text
from bs4 import BeautifulSoup
from bs4.element import ProcessingInstruction
from pandas.core.algorithms import unique
import requests


df = pd.read_csv('Players_447.csv')


df.columns = df.columns.str.replace(' ','_')
df.drop('Unnamed:_0',axis = 1,inplace=True)
i = int(0)



for a in df.iterrows():
    if df.loc[i,'Version'] != 'futhero' and df.loc[i,'Version'] != 'gold' and df.loc[i,'Version'] != 'silver' and df.loc[i,'Version'] != 'gold-nr' and df.loc[i,'Version'] != 'silver-nr' and df.loc[i,'Version'] != 'icon':
        df.loc[i,'Version'] = 'special'
    i+=1    

i=int(0)


df.loc[df['Version'] == 'futhero', 'Team'] = 'Hero'
df.loc[df['Position'] == 'RWB', 'Position'] = 'RB'
df.loc[df['Position'] == 'LWB', 'Position'] = 'LB'
df.loc[df['Position'] == 'RF', 'Position'] = 'RW'
df.loc[df['Position'] == 'RM', 'Position'] = 'RW'
df.loc[df['Position'] == 'LF', 'Position'] = 'LW'
df.loc[df['Position'] == 'LM', 'Position'] = 'LW'


uniPos = []
uniVers = []
uniTeam = []
uniLeague = []
uniWR = []
uniSF = []



for a in df.iterrows():
    if df.loc[i,'Position'] not in uniPos:
        uniPos.append(df.loc[i,'Position'])

    if df.loc[i,'Version'] not in uniVers:
        uniVers.append(df.loc[i,'Version'])

    if df.loc[i,'Team'] not in uniTeam:
        uniTeam.append(df.loc[i,'Team'])

    if df.loc[i,'League'] not in uniLeague:
        uniLeague.append(df.loc[i,'League'])

    if df.loc[i,'Work_Rates'] not in uniWR:
        uniWR.append(df.loc[i,'Work_Rates'])

    if df.loc[i,'Strong_Foot'] not in uniSF:
        uniSF.append(df.loc[i,'Strong_Foot'])

    i = i+1


i = int(0)

for a in df.iterrows():
    df.loc[i,'In_Games'] = df.loc[i,'In_Games'].replace(',','')
    df.loc[i,'Position'] = uniPos.index(df.loc[i,'Position'])
    df.loc[i,'Version'] = uniVers.index(df.loc[i,'Version'])
    df.loc[i,'Team'] = uniTeam.index(df.loc[i,'Team'])
    df.loc[i,'League'] = uniLeague.index(df.loc[i,'League'])
    df.loc[i,'Work_Rates'] = uniWR.index(df.loc[i,'Work_Rates'])
    df.loc[i,'Strong_Foot'] = uniSF.index(df.loc[i,'Strong_Foot'])
    i = i+1

i = int(0)

for a in df.iterrows():
    if type(df.loc[i,'Price']) == float:
        i+=1
        continue

    if (df.loc[i,'Price'][-1]) == 'K':
        y = int(float((df.loc[i,'Price'].replace(df.loc[i,'Price'][-1],''))) * 1000)
        df.loc[i,'Price'] = y
        i+=1
        continue
        

    if (df.loc[i,'Price'][-1]) == 'M':
        x = (int(float(df.loc[i,'Price'].replace(df.loc[i,'Price'][-1],''))*1000000))
        df.loc[i,'Price'] = x
        i+=1
        continue

    i+=1

df = df.dropna()


Change = ['Position', 'Price', 'Version', 'Team', 'League', 'Work_Rates', 'Strong_Foot', 'In_Games']    
    
for a in Change:
    df[a] = df[a].apply(pd.to_numeric)




df.to_csv('Players_Edited.csv')

print('done')