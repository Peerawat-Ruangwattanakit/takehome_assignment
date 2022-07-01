import requests
from requests import Session
import time

def price_from_coinmarketcap(symbol:str) -> float:
    """
    This function will receive symbol and return price of symbol from Coinmarketcap.
    :param symbol(str)
    :return price(float) if it not have in Coinmarketcap It will return 'error'
    """

    def find_slug(symbol:str) -> str:
        """
        This function will receive symbol and return slug name of symbol from Coinmarketcap.
        Slug name is necessary to get price from Coinmarketcap.
        :param symbol(str)
        :return slug_name(str) if it not have name in Coinmarketcap It will return 'error'
        """

        API_KEY = 'd608c643-5128-4df0-a76c-5ba15fe3d362'
        url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        parameters = {
            'symbol':symbol
            }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': API_KEY
            }
        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            if response.status_code == 429:
                time.sleep(60)
                return 'try'
            slug = response.json()["data"][0]["slug"]
            return slug
        except Exception as e:
            return 'error'

    API_KEY = '59769d5a-7321-4ae8-8f5f-bfd77559389a'
    slug = find_slug(symbol)
    if slug=='try':
        slug = find_slug(symbol)
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
        'slug':slug,
        'convert':'USD'
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
        }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        if response.status_code == 429:
            time.sleep(60)
            return 'try'
        for key in response.json()['data'].keys():
            ask_price = float(response.json()["data"][key]['quote']['USD']['price'])
    except Exception as e:
        return 'error'
    return ask_price