1.Outlier
When I study statistic in university, There are 2 popular way to find outlier. First is find using 2 S.D. and second is 1.5 IQR, both way usually get same result. 1.5 IQR need Q1 and Q3 to calculate but we only have atleast 3 source, so it not suit for this problem. From that reason, I find outlier by using 2SD,so data that not inside +- 2SD are outlier.

2.What would I do if I have more time?
2.1 Change price that get from binance be USD instead of stable coin BUSD. Because Binance API don't have way to get usd price directly ,so I need to get BUSD price and send to other 4 API to get USD price of BUSD, but it will reach limit and I can't use other API that test didn't give me.
