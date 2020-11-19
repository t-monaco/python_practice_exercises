import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys


my_hacker_news = []
n_pages = int(sys.argv[1])


def sort_news_by_points(hn_list):
    return sorted(hn_list, key=lambda k: k['points'], reverse=True)


def custom_hn(links, subtext):
    new_hn = []
    for key, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = int(subtext[key].select('.score')[0].getText().replace(' points', ''))
        if vote and vote > 99:
            new_hn.append({'title': title, 'link': href, 'points': vote})

    return new_hn


for i in range(1, n_pages + 1):
    res = requests.get(f'https://news.ycombinator.com/news?p={i}')
    soup = BeautifulSoup(res.text, 'html.parser')
    soup_links = soup.select('.storylink')
    soup_subtext = soup.select('.subtext')

    result = custom_hn(soup_links, soup_subtext)

    for i in result:
        my_hacker_news.append(i)


pprint(sort_news_by_points(my_hacker_news))
