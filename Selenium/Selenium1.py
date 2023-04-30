from selenium import webdriver
from selenium.webdriver.chrome.service import Service
website='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation='
path=Service("E:/chromeDriver/chromedriver.exe")

driver=webdriver.Chrome(service=path)
driver.get(website)
driver.maximize_window()
#driver.close()