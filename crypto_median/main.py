from typing import List
from .calculator import calculate_median
from .handler import find_price

def find_median_of_symbols(symbols: List[str]) -> float:
    """
    This function will receive list of symbol and return median of that list.
    :param List of symbol
    :return median of input list without outlier but if it not have enough source It will be 'Not enough source'
    """

    symbols = list(set(symbols))
    for symbol in symbols:
        try:
            price_list=find_price(symbol)
            if price_list == 'Not enough source':
                print(symbol,'Not enough source')
            else:
                med=calculate_median(price_list)
                print(symbol,med)
        except Exception as e:
            raise e
