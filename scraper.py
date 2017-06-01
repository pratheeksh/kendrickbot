import random
from time import sleep

import requests
from bs4 import BeautifulSoup, SoupStrainer

AZ_BASE_URL = 'http://www.metrolyrics.com/'
kendrick_urls = ['http://www.metrolyrics.com/kendrick-lamar-alpage-1.html',
                 "http://www.metrolyrics.com/kendrick-lamar-alpage-2.html",
                 "http://www.metrolyrics.com/kendrick-lamar-alpage-3.html"]


def get_file():
    for kendrick_url in kendrick_urls:
        response = requests.get(kendrick_url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/35.0.1916.153 Safari/537.36'})
        for link in BeautifulSoup(response.text, "html.parser", parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                if "lyrics-kendrick-lamar" in (link['href']):
                    with open('kendrick.txt', 'a') as fd:
                        lyrics = get_lyrics(link['href'])
                        fd.write(lyrics)


def get_lyrics(url):
    print('Getting lyrics from {}'.format(url))
    try:
        sleep(random.randint(0, 20))
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/35.0.1916.153 Safari/537.36'})
        soup = BeautifulSoup(response.text, "html.parser")
        page_lyric = soup.find("div", {"id": "lyrics-body-text", "class": "js-lyric-text"})
        page_lyric = page_lyric.get_text()
        return page_lyric
    except:
        "some error occured"


if __name__ == '__main__':
    get_file()
