import requests

def price_from_coingecko(symbol:str) -> float:
    """
    This function will receive symbol and return price of symbol from Coingecko.
    :param symbol(str)
    :return price(float) if it not have in Coingecko It will return 'error'
    """

    url='https://api.coingecko.com/api/v3/search?query='+symbol
    response = requests.get(url)
    try:
        symbol_fullname = response.json()["coins"][0]['id']
    except:
        return 'error'
    url='https://api.coingecko.com/api/v3/simple/price?ids='+symbol_fullname+'&vs_currencies=usd'
    response = requests.get(url)
    try:
        ask_price = response.json()[symbol_fullname]['usd']
    except:
        return 'error'
    return ask_price