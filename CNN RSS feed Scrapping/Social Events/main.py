import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://rss.cnn.com/rss/edition_world.rss'
response = requests.get(url)
soup = BeautifulSoup(response.content, features='xml')
print(soup.prettify())
items = soup.find_all('item')
headline = []
date = []
description = []
for item in items:
    if item.title in item:
        headline.append(item.title.text)
    if item.pubDate in item:
        date.append(item.pubDate.text)
    if item.description in item:
        description.append(item.description.text)

df = pd.DataFrame(list(zip(headline, date, description)), columns=['Headline','Publish Date & Time','Description'])
df.to_csv('D:/Epicenter-News-Research/CNN RSS feed Scrapping/Social Events/social_events.csv')