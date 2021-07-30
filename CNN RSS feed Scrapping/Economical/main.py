import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://rss.cnn.com/rss/money_news_international.rss'
res = requests.get(url)
soup = BeautifulSoup(res.content, features='html.parser')
print(soup.prettify())
items = soup.find_all('item')
headline = []
pub_date = []
des = []
for item in items:
    headline.append(item.title.text)
    pub_date.append(item.pubdate.text)
    des.append(item.description.text.split('<img')[0])

df = pd.DataFrame(list(zip(headline, pub_date, des)), columns=['Headline','Publish Date & Time','Description'])
df.to_csv('D:/Epicenter-News-Research/CNN RSS feed Scrapping/Economical/economical.csv')
