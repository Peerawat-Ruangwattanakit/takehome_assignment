from gettext import find
from lib2to3.pygram import Symbols
from msilib.schema import Class
import unittest
from crypto_median.handler import find_price
from crypto_median.handler.all_api import *
import json
import os
class TestAPI(unittest.TestCase):
    def test_len_price(self):
        """
        Check that price from API are not missing from some API
        """

        symbols = [
            "BTC", "ETH", "USDT", "USDC", "BNB", "BUSD", "ADA", "XRP",
            "SOL", "DOT", "DOGE", "DAI", "AVAX", "MATIC", "NEAR", 
            "ALGO", "UNI", "HBAR", "ICP", "XTZ", "FIL", "APE", "CAKE",
            "SUSHI", "BAND", "OP", "MOVR", "BAND", "ALPHA"
            ]
        with open(os.path.join(os.path.dirname(__file__), "test_case_len.json"), "r") as json_file:
            data = json.load(json_file)
            for symbol in symbols:
                price_list = find_price(symbol)
                self.assertEqual(len(price_list),data[symbol])

if __name__ == '__main__':
    unittest.main()