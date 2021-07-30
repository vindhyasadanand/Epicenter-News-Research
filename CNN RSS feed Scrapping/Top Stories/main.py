import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://rss.cnn.com/rss/edition.rss'
res = requests.get(url)
soup = BeautifulSoup(res.content, features='html.parser')
print(soup.prettify())
items = soup.find_all('item')
headline = []
pub_date = []
des = []
for item in items:
    if item.title in item:
        headline.append(item.title.text)
    if item.pubdate in item:
        pub_date.append(item.pubdate.text)
    if item.description in item:
        des.append(item.description.text)

df = pd.DataFrame(list(zip(headline, pub_date, des)), columns=['Headline','Publish Date','Description'])
df.to_csv('D:/Epicenter-News-Research/CNN RSS feed Scrapping/Top Stories/output.csv')