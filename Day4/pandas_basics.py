# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:01:46 2019

@author: KUKUMAR
"""

import pandas as pd
import matplotlib.pyplot as plot 

d1 = {'year':[2010,2011,2012,2013,2014],
      'stock':[1010,2020,4040,6000,5500]}

print(d1)
print(d1["stock"])

data = pd.DataFrame(d1)

print(data.stock[3])


plot.bar(data.year,data.stock)
#OR Can be written as plot.bar(data["YEAR"],data["STOCK"])
plot.xlabel("Years")
plot.ylabel("Stocks")
plot.show()


plot.plot(data["year"],data["stock"],marker="*")
plot.xlabel("Years")
plot.ylabel("Stocks")
plot.show()

#print(data)

print(type(data.to_dict()))
print(data.to_dict())

print(data)

print(data.max())

print(data.describe())

"""
print(type(data))
#<class 'pandas.core.frame.DataFrame'>

print(type(data.stock))
#<class 'pandas.core.series.Series'>

print(type(data['stock']))
#<class 'pandas.core.series.Series'>


"""
