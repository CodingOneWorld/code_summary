# -*- coding: utf-8 -*-

import  warnings
warnings.filterwarnings('ignore')

import pandas as pd

# 显示所有行(参数设置为None代表显示所有行，也可以自行设置数字)
pd.set_option('display.max_columns', None)
# 显示所有列
pd.set_option('display.max_rows', None)
# 设置数据的显示长度，默认为50
pd.set_option('max_colwidth', 200)
# 禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)

# 启发式搜索 递归特征消除
### 生成数据
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000,         # 样本个数
                           n_features=25,          # 特征个数
                           n_informative=3,        # 有效特征个数
                           n_redundant=2,          # 冗余特征个数（有效特征的随机组合）
                           n_repeated=0,           # 重复特征个数（有效特征和冗余特征的随机组合）
                           n_classes=8,            # 样本类别
                           n_clusters_per_class=1, # 簇的个数
                           random_state=0)

### 特征选择
# RFE
from sklearn.svm import SVC
svc = SVC(kernel="linear")

from sklearn.feature_selection import RFE
rfe = RFE(estimator = svc,           # 基分类器
          n_features_to_select = 2,  # 选择特征个数
          step = 1,                  # 每次迭代移除的特征个数
          verbose = 0                # 显示中间过程
          ).fit(X,y)
X_RFE = rfe.transform(X)
print(X_RFE)
print(X[0])
print("RFE特征选择结果——————————————————————————————————————————————————")
print("有效特征个数 : %d" % rfe.n_features_)
print("全部特征等级 : %s" % list(rfe.ranking_))

# RFECV
from sklearn.svm import SVC
svc = SVC(kernel="linear")

from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
rfecv = RFECV(estimator=svc,          # 学习器
              min_features_to_select=2, # 最小选择的特征数量
              step=1,                 # 移除特征个数
              cv=StratifiedKFold(2),  # 交叉验证次数
              scoring='accuracy',     # 学习器的评价标准
              verbose = 0,
              n_jobs = 1
              ).fit(X, y)
X_RFECV = rfecv.transform(X)
print("RFECV特征选择结果——————————————————————————————————————————————————")
print("有效特征个数 : %d" % rfecv.n_features_)
print("全部特征等级 : %s" % list(rfecv.ranking_))