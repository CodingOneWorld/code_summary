"""
用省市扩充已有关键词
"""

import pandas as pd

df=pd.read_excel('全国省份和地级市划分.xlsx')
print(df.head())
province=df['省份名称'].values
print(province)

#



