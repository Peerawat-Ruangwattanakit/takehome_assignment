import requests

def price_from_okx(symbol:str) -> float:
    """
    This function will receive symbol and return price of symbol from Okx.
    :param symbol(str)
    :return price(float) if it not have in Okx It will return 'error'
    """

    url='https://www.okx.com/api/v5/market/ticker?instId='+symbol+'-USD-SWAP'
    response = requests.get(url)
    try:
        ask_price=float(response.json()['data'][0]['askPx'])
        return ask_price
    except Exception as e:
        return 'error'