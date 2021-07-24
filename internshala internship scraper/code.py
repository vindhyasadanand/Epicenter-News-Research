from bs4 import BeautifulSoup
import requests
import pandas as pd

data = requests.get('https://internshala.com/internships/computer%20science-internship').text
soup = BeautifulSoup(data, 'html.parser')

intern_header = soup.find_all('div', class_='company')
locations = soup.find_all('a', class_='location_link')
intern_details = soup.find_all('div', class_='internship_other_details_container')

company = []
pro = []
loc = []
sti = []
li = []
for header, location, details in zip(intern_header, locations, intern_details):
    company_name = header.find('a', 'link_display_like_text').text.replace(" ","")
    company.append(company_name)
    profile = header.find('a').text
    pro.append(profile)
    link = header.find('a').get('href')
    li.append(link)
    stipend = details.find('span', class_='stipend').text
    sti.append(stipend)
    loc.append(location.text)
    print("Company Name: ", company_name )
    print("Profile: ", profile)
    print("Location: ", location.text)
    print("Stipend: ", stipend)
    print("Link: ", link)
    print("-----------------------------------------------------------------------------------------------------------------")

df = pd.DataFrame(list(zip(company, pro, loc, sti, li)), columns=['Company Name', 'Profile', 'Location', 'Stipend', 'Link'])
df.to_csv("data.csv")








