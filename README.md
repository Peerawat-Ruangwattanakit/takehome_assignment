# How to use this package?

1.Put crypto_median folder to your

	/Python3X/Lib/site-packages

2.Open python and write code
	
```
from crypto_median import find_median_of_symbols
find_median_of_symbols([<List of symbols>]) #find_median_of_symbols(["ETH","BTC"])
```

3.Run and code will prine median price.

--------------------------------------------------------------
# 1.Outlier
When I study statistic in university, There are 2 popular way to find outlier. First is find using 2 S.D. and second is 1.5 IQR, both way usually get same result. 1.5 IQR need Q1 and Q3 to calculate but we only have atleast 3 source, so it not suit for this problem. From that reason, I find outlier by using 2SD, so data that not inside +- 2SD are outlier.

# 2.What would I do if I have more time?
2.1 Change price that get from binance be USD instead of stable coin BUSD.

Because Binance API don't have way to get usd price directly ,so I need to get BUSD price and send to other 4 API to get USD price of BUSD, but it will reach limit and I can't use other API that test didn't give me.	

2.2 Create and use custom error in structs folder.

I think it is not high priority for functional so I put this after anything and didn't finish in time.

2.3 Find way to send list of symbols instead one symbol.

I know that I only send one symbol per request but some API like Binance have some problem when I request with bulk API(list of symbol). When you send with list of symbol, if some symbol didn't have in their platform it will response only "One response" that your symbol have a problem, so I need to send request with only one symbol per time to avoid that problem. 

2.4 Rate Limit

CoinGecko have worst API rate limit only 30/min so that why I only need code to sleep when CoinGecko reach limit because other API is impossible to reach limit before Coingecko. But I know that you need to handle other API too for rate limit, so if I have time I will handle on other API too.

2.5 wrapper.py
I don't know that wrapper.py that you want are need to write with decorator so I just wrap all API in this code instead, and I think my wrapper is very bad for extended it in future. If I have more time I will use decorator instead of list of function.
