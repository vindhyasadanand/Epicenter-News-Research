from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://internshala.com/internships/computer%20science-internship'
i = 0
company = []
pro = []
loc = []
sti = []
li = []
while i<63:
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    intern_header = soup.find_all('div', class_='company')
    locations = soup.find_all('a', class_='location_link')
    intern_details = soup.find_all('div', class_='internship_other_details_container')
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
    i+=1
    s = str(i)
    url_tag = "/page-"+s
    url = 'https://internshala.com/internships/computer%20science-internship'+url_tag


df = pd.DataFrame(list(zip(company, pro, loc, sti, li)), columns=['Company Name', 'Profile', 'Location', 'Stipend', 'Link'])
df.to_csv("data.csv")
















