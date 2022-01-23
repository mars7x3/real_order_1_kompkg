
import requests

from bs4 import BeautifulSoup
from decimal import Decimal as D
from decouple import config



def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url,headers=headers)
    return response.text


def get_price(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        price = soup.find('span', class_='price').text[:-4]
        return D(price)
    except AttributeError:
        return None


def main(article):
    url = config('my_url') + f'%D0%BF%D0%BE%D0%B8%D1%81%D0%BA?keyword={article}&advanced_search_categories=&advanced_search_price_min=0&advanced_search_price_max=0&advanced_search_currency=USD&limitstart=0&option=com_virtuemart&view=category'
    return get_price(get_html(url))


