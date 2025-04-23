# -*- coding: utf-8 -*-
import pandas as pd

# 读取文件  加入新的否定词  去重再写回文件
df=pd.read_csv('洗地机否定词.csv')
print(df.head())
df_s=set(df['no_key_word'].values)
print(df_s)
# 字符串去重
# 提取否定词
# s='''
# CROSSMAVE、必胜、石头、UWANT、悠尼、Shark、UOSU、TLXT、Greenhome
# 摩根、米博、亮神、欧莱特、黑德、菲沃斯、浠美洁、双幼、荣事达、家小优
# 顺造、福维克、斯帝沃、伊莱克斯、小米、CEYEE 希亦、美的、Haier 海尔、西屋、扬子、莱克、顺造、森电、德尔玛、斐纳、松下、飞利浦、科沃斯、博世、滴水大白、凯驰'''
# s_l=set(s.replace('\n','').strip('\n').split('、'))
# print(len(s_l))
# print(s_l)
# for i in s_l:
#     print(i)

s_l={'美的','联想','以内','顺造','荣事达','greenhome','德尔玛','必胜','法普顿'}

# 去重，再写回文件
s_final=df_s | s_l
print(len(s_final))
# print(s_final)
for s in s_final:
    print(s)

df_new=pd.DataFrame(list(s_final),columns=['no_key_word'])
df_new.to_csv('洗地机否定词.csv',index=0)