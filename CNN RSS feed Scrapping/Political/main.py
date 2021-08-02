import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://rss.cnn.com/rss/cnn_allpolitics.rss'
res = requests.get(url)
soup = BeautifulSoup(res.content, features='html.parser')
print(soup.prettify())
items = soup.find_all('item')

headline = []
pub_date = []
des = []
for i in range(len(items)):
    if items[i].title in items[i]:
        headline.append(items[i].title.text)
    if items[i].pubdate in items[i]:
        pub_date.append(items[i].pubdate.text)
    if items[i].description in items[i]:
        des.append(items[i].description.text)

df = pd.DataFrame(list(zip(headline, pub_date, des)), columns=['Headline','Publish Date & Time','Description'])
df.to_csv('D:/Epicenter-News-Research/CNN RSS feed Scrapping/Political/political.csv')