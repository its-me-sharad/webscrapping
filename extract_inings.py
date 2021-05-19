from bs4 import BeautifulSoup
import requests
import pandas as pd

Name = []
Runs = []
Minutes = []
Ball_Faced = []
Fours = []
Sixes = []
SR = []
Inns = []
Opposition = []
Ground = []
Date = []

raw_data = requests.get('https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;orderby=start;orderbyad=reverse;spanmin1=05+Jan+2011;spanval1=span;team=6;template=results;type=batting;view=innings').text
soup = BeautifulSoup(raw_data, 'lxml')
#print(soup)
players = soup.find_all('tr', class_='data1')
#print(players)
for player in players:
    individual = player.find_all('td')
    Name.append(individual[0].text)
    Runs.append(individual[1].text)
    Minutes.append(individual[2].text)
    Ball_Faced.append(individual[3].text)
    Fours.append(individual[4].text)
    Sixes.append(individual[5].text)
    SR.append(individual[6].text)
    Inns.append(individual[7].text)
    Opposition.append(individual[9].find('a').text)
    Ground.append(individual[10].find('a').text)
    Date.append(individual[11].text)

df = pd.DataFrame(list(zip(Name, Runs, Minutes, Ball_Faced, Fours, Sixes, SR, Inns, Opposition, Ground, Date)), columns=['Name', 'Runs', 'Mins', 'Ball_Faced', 'Fours', 'Sixes', 'SR', 'Inns', 'Opposition', 'Ground', 'Date'])
df.to_csv('India.csv', index=False)

