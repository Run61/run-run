# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:01:49 2021

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader.data as web

def price(stock, start):
    price = web.DataReader(name=stock, data_source='yahoo', start=start)['Adj Close']
    return price.div(price.iat[0]).resample('M').last().to_frame('price')

a = price('SPY','2000-01-01')
print(a)
'''
def fractal(a, p):
    df = pd.DataFrame()
    for count in range(1,p+1):
        a['direction'] = np.where(a['price'].diff(count)>0,1,0)
        a['abs'] = a['price'].diff(count).abs()
        a['volatility'] = a.price.diff().abs().rolling(count).sum()
        a['fractal'] = a['abs']/a['volatility']*a['direction']
        df = pd.concat([df, a['fractal']], axis=1)
    return df

def meanfractal(a, l=12):
    a['meanfractal']= pd.DataFrame(fractal(a, l)).sum(1,skipna=False)/l
    mean_shift = a['meanfractal'].shift(1)
    price_shift = a['price'].shift(1)
    factor = 1.03**(1/l)
    a['portfolio1'] = (a['price']/price_shift*mean_shift+(1-mean_shift)*factor).cumprod()
    a['portfolio2'] = ((a['price']/price_shift*mean_shift+factor)/(1+mean_shift)).cumprod()
    a.dropna(inplace=True)
    a = a.div(a.ix[0])
    return a[['price','portfolio1','portfolio2']].plot() 

print(a)
plt.show()
meanfractal(a)
'''