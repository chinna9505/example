import requests
from bs4 import BeautifulSoup
import pandas as pd


class NewsReading:
    def newsfromhyd(self):
        url = "https://news.google.com/search?q=hyderabad"
        response = requests.get(url)
        # print(response.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        for head in headlines:
            print(head.text)
            print(head.text.strip())
        # main = head.text
        lines = {'urls': [url], 'columns' : [head]}
        df = pd.DataFrame(lines)
        print(df)




