# -*- coding: utf-8 -*-

# 导入要使用的库
import pandas as pd
import numpy as np
# 创建一个包含两个变量的数据集
data = {
'Gender': ['Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female'],
'Smoker': ['Smoker', 'Smoker', 'Non-Smoker', 'Non-Smoker', 'Smoker', 'Smoker', 'Non-Smoker', 'Non-Smoker']
}
df = pd.DataFrame(data)
print(df)

data=df[df['Gender']=='Male']['Smoker'].values
print(data)


# # 生成列联表
# crosstab_result = pd.crosstab(df['Gender'], df['Smoker'])
# # 打印结果
# print(crosstab_result)
# print(crosstab_result.values)
#
# # 卡方检验
# from  scipy.stats import chi2_contingency
#
# # 接收的是列联表 dataframe
# kt=chi2_contingency(crosstab_result)
#
# print('卡方值=%.4f, p值=%.4f, 自由度=%i expected_frep=%s'%kt)
