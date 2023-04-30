from bs4 import BeautifulSoup
import requests
request = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=').text
soup=BeautifulSoup(request,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').text
    if 'few' in published_date:
        institution = job.h3.text.replace(' ', '')
        locations = job.span.get_text(strip=True,separator=' ')
        description = job.li.get_text(strip=True,separator=' ')
        skills = job.find('span',class_='srp-skills').get_text(strip=True,separator=' ')
        link=job.a['href']
        print(f"{institution.strip()}:")
        print(f"has the location: {locations}")
        print(f"must have: {skills} skills")
        print(f"{published_date.strip()}")
        print(f'for more info click:{link}')

        print('')
