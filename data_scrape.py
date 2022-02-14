import requests
from bs4 import BeautifulSoup
import message
import time

def data_scrape():
    baseUrl = "https://www.espncricinfo.com/"
    time.sleep(2)
    page = requests.get(baseUrl).text

    soup = BeautifulSoup(page, 'html.parser')

    status = soup.find_all(
        class_="match-info")[0].find_all(class_="status")[0].text
    teams = soup.find_all(class_="match-info")[0].find_all(class_="teams")[0]
    team_one = teams.find_all('div')[0].find_all(class_="team")[0]
    team_two = teams.find_all('div')[0].find_all(class_="team")[1]
    team_one_name = team_one.find_all(class_="name-detail")[0].text
    try:
        team_one_score = team_one.find_all(class_="score-detail")[0].text
    except:
        team_one_score = ""

    team_two_name = team_two.find_all(class_="name-detail")[0].text
    try:
        team_two_score = team_two.find_all(class_="score-detail")[0].text
    except:
        team_two_score = ""
    status_text = soup.find_all(
        class_="match-info")[0].find_all(class_="status-text")[0].text

    result = f'{status}\n{team_one_name}  {team_one_score} \n {team_two_name}   {team_two_score} \n {status_text}'
    message.send_msg(result)
    print(result)
