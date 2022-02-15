import requests
import message
from bs4 import BeautifulSoup

all_status = list()
all_desc_f = list()
all_team_one = list()
all_team_two = list()
all_team_one_score = list()
all_team_two_score = list()
all_status_text = list()

def all_result():
    response = requests.get(
        "https://www.espncricinfo.com/series/pakistan-super-league-2021-22-1292999/match-schedule-fixtures")

    soup = BeautifulSoup(response.text, "html.parser")

    all_table = soup.find_all(class_="container-fluid")[0]
    all_descriptions = all_table.find_all(class_="description")
    status = all_table.find_all(class_="status")
    for stat in status:
        all_status.append(stat.text)
    for desc in all_descriptions:
        if desc.text.startswith("Check"):
            continue
        else:
            all_desc_f.append(desc.text)

    all_teams = all_table.find_all(class_="teams")
    for team in all_teams:
        team_one = team.find_all(class_="name-detail")[0].text
        team_two = team.find_all(class_="name-detail")[1].text
        try:
            team_one_score = team.find_all(class_="score-detail")[0].text
        except:
            team_one_score = ""

        try:
            team_two_score = team.find_all(class_="score-detail")[1].text
        except:
            team_two_score = ""

        all_team_one_score.append(team_one_score)
        all_team_two_score.append(team_two_score)
        all_team_one.append(team_one)
        all_team_two.append(team_two)

    status_text = all_table.find_all(class_="status-text")
    for stat in status_text:
        all_status_text.append(stat.text)

def all_matches():
    result = str()  
    for i in range(0, len(all_status)-1):
        result += f'{all_status[i]}\n{all_desc_f[i]}\n{all_team_one[i]}     {all_team_one_score[i]}\n{all_team_two[i]}        {all_team_two_score[i]}\n{all_status_text[i]}'
        result += "\n--\n"
    send_message(result)    


def live_matches():
    result = str()
    for i,stat in enumerate(all_status):
        if stat == "live":
            result += f'{all_status[i]}\n{all_desc_f[i]}\n{all_team_one[i]}     {all_team_one_score[i]}\n{all_team_two[i]}        {all_team_two_score[i]}\n{all_status_text[i]}'
            send_message(result)
            return
    result = "There is no live match currently"        
    send_message(result)

def send_message(result):
    if(len(result) >= 1600):
        message.send_msg(result[0:1599])
        message.send_msg(result[1600:len(result)])    
    else:
        message.send_msg(result)