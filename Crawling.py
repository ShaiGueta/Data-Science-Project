import pandas as pd
from pandas import DataFrame
from typing import Text
from bs4 import BeautifulSoup
from bs4.element import ProcessingInstruction
import requests

#(player_name, overall, position,version, price, nation, team, league, pace, shot, passing, drib, deff, phy, skill_move ,weak_foot,work_rates , strong_foot, in_games)
p=int(0)

Name_List = []
Rating_List = []
Position_List = []
Price_list = []
Version_List = []
Nation_list = []
Team_list = []
League_list = []
Pace_list = []
Shot_list = []
Passing_list = []
Drib_List = []
Deff_List = []
Phy_List = []
SM_List = []
WF_List = []
WR_List = []
Strong_Foot_List = []
In_Games_List = []


while p<447:
    url_start = 'https://www.futwiz.com/en/fifa22/players?page='
    page_num = str(p)
    url = url_start + page_num


    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text,'lxml')

    all_rows = soup.find_all('tr', class_ = 'table-row')
    j=int(0)
    table_row = all_rows[j]


    for i in all_rows:
        table_row = all_rows[j]
        stand_alone = table_row.find_all('td')

        player_name = table_row.find('p', class_='name').text.replace(' ','').replace('\n','')
        Name_List.append(player_name)
        overall = table_row.find('td', class_='ovr').text.replace(' ','').replace('\n','')
        Rating_List.append(overall)
        position = stand_alone[3].text.replace(' ','').replace('\n','')
        Position_List.append(position)
        price = stand_alone[4].text.replace(' ','').replace('\n','')
        Price_list.append(price)
        ver = table_row.find('div', class_='otherversion22')['class'][1]
        version = ver[ver.find('-')+1:]
        Version_List.append(version)
        img = table_row.find('img', class_ = 'nation')
        nation = img['src'][img['src'].rfind('/')+1:img['src'].rfind('.png')]
        Nation_list.append(nation)
        TeamLeague = table_row.find('p',class_ = 'team' ).text.replace('\n','')
        team = TeamLeague[0:TeamLeague.find('|')].strip()
        Team_list.append(team)
        league = TeamLeague[TeamLeague.find('|')+1:].strip()
        League_list.append(league)
        stats = table_row.find_all('span', class_ = 'stat')
        pace = stats[0].text
        Pace_list.append(pace)
        shot = stats[1].text
        Shot_list.append(shot)
        passing = stats[2].text
        Passing_list.append(passing)
        drib = stats[3].text
        Drib_List.append(drib)
        deff = stats[4].text
        Deff_List.append(deff)
        phy = stats[5].text
        Phy_List.append(phy)
        stars = table_row.find_all('span', class_='starRating')
        skill_move = stars[0].text.replace(' ','').replace('\n','')
        SM_List.append(skill_move)
        weak_foot = stars[1].text.replace(' ','').replace('\n','')
        WF_List.append(weak_foot)
        work_rates = table_row.find('span', class_='wrs').text.replace(' ','').replace('\n','')
        WR_List.append(work_rates)
        strong_foot = stand_alone[14].text.replace(' ','').replace('\n','')
        Strong_Foot_List.append(strong_foot)
        in_games = stand_alone[15].text.replace(' ','').replace('\n','')
        In_Games_List.append(in_games)
        #print(player_name, overall, position,version, price, nation, team, league, pace, shot, passing, drib, deff, phy, skill_move ,weak_foot,work_rates , strong_foot, in_games)
        j+=1
    p+=1


Data = {
    'Name' : Name_List, 'Rating' : Rating_List, 'Position' : Position_List, 'Price':Price_list, 'Version':Version_List, 'Nation':Nation_list, 'Team': Team_list, 'League': League_list,
    'Pace': Pace_list, 'Shot':Shot_list, 'Pass':Passing_list,'Drib':Drib_List, 'Deff':Deff_List, 'Phy':Phy_List,'Skill_Moves':SM_List,'Weak_Foot':WF_List,'Work_Rates':WR_List,
    'Strong_Foot':Strong_Foot_List, 'In_Games':In_Games_List
}

df = pd.DataFrame(Data)

df.to_csv('Players_447.csv')

print('Done!')