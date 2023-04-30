from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = Service("E:/chromeDriver/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get(website)
# driver.maximize_window()

dates = []
home_team = []
scorecard = []
away_team = []

tags = driver.find_elements(By.TAG_NAME, 'tr')
for tag in tags:
    date = tag.find_element(By.XPATH, './td[1]').text
    dates.append(date)
    print(date)
    home_teams = tag.find_element(By.XPATH, './td[2]').text
    home_team.append(home_teams)
    scorecards = tag.find_element(By.XPATH, './td[3]').text
    scorecard.append(scorecards)
    away_teams = tag.find_element(By.XPATH, './td[4]').text
    away_team.append(away_teams)


driver.quit()
dict = {'Dates': dates, 'Home_teams': home_team, 'Score': scorecard, 'Away_team': away_team}
df = pd.DataFrame(dict)
df.to_csv('Football_data.csv')


