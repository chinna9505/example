from base.news_reding import NewsReading

def news_print():
    news = NewsReading()
    return news.newsfromhyd()


if __name__ == '__main__':
    news_print()
