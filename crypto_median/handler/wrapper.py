from .all_api import *
from typing import List

LIMIT_ERROR_SOURCE = 2

func_list = [
    price_from_binance,
    price_from_coingecko,
    price_from_coinmarketcap,
    price_from_kraken,
    price_from_okx
    ]

def find_price(symbol: str) -> List[float]:
    """
    This function will receive symbol and return price of symbol from all API.
    :param symbol(str)
    :return list of price(List(float)) if it not have enough sorce it return 'Not enough source'
    """

    error_count = 0
    price_list = []
    for f in func_list:
        ask_price = f(symbol)
        if ask_price == 'try':
            ask_price = f(symbol)
        if ask_price == 'error':
            error_count=error_count+1
        else:
            price_list.append(ask_price)
        if error_count > LIMIT_ERROR_SOURCE:
            
            #Problem say I need to throw error but I don't know that you need me
            #to raise or just print error so if it raise just delete sharp symbol below.

            #raise Exception("Not enough source")
            return 'Not enough source'
    return price_list
