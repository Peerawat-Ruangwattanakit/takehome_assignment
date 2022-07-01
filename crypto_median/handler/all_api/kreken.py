import requests

def price_from_kraken(symbol:str) -> float:
    """
    This function will receive symbol and return price of symbol from Kraken.
    :param symbol(str)
    :return price(float) if it not have in Kraken It will return 'error'
    """

    url='https://api.kraken.com/0/public/Ticker?pair='+symbol+'USD'
    response = requests.get(url)
    try:
        for key in response.json()['result'].keys():
            ask_price = float(response.json()['result'][key]['a'][0])
        return ask_price
    except Exception as e:
        return 'error'