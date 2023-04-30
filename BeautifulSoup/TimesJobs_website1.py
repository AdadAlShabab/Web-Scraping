from bs4 import BeautifulSoup
import requests

request = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=').text
# print(request)
soup = BeautifulSoup(request, 'lxml')
# li_tag=soup.find('li')
# print(li_tag)
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
details = soup.find('ul', 'list-job-dtl clearfix')

for job in jobs:
    institution = job.h3.text.replace(' ', '')
    locations = job.span.text
    description = details.li.text
    skills = details.span.text.replace(' ', '')
    published_date = job.find('span', class_='sim-posted').text
    print(
        f'''{institution}: has the location: {locations} & must have {skills}skills which is posted{published_date}''')
