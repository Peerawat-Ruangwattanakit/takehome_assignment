from urllib import response
import requests
def price_from_binance(symbol:str) -> float:
    """
    This function will receive symbol and return price of symbol from binance.
    :param symbol(str)
    :return price(float) if it not have in Binance It will return 'error'
    """

    if symbol == "BUSD":
        return 1.0
    url='https://www.binance.com/api/v3/ticker/price?symbol='+symbol+"BUSD"
    response = requests.get(url)
    try:
        ask_price = float(response.json()['price'])
        return ask_price
    except Exception as e:
        return 'error'