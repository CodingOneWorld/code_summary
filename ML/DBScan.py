# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib.colors

# 设置属性防止中文乱码及拦截异常信息
# 查看当前系统已经安装的字体，方便在全局设置中使用字体名称
fontnamelist = font_manager.get_font_names()
# print(fontnamelist)

mpl.rcParams['font.sans-serif'] = [u'Songti SC']
mpl.rcParams['axes.unicode_minus'] = False

# 构造数据
N = 1000
centers = [[1, 2], [-1, -1], [1, -1], [-1, 1]]
X, y1 = make_blobs(N, n_features=2,
                          centers=centers, cluster_std=(1, 0.75, 0.5, 0.25), random_state=0)
X = StandardScaler().fit_transform(X)

# 参数与聚类
eps=0.2
min_samples=12

model = DBSCAN(eps=eps, min_samples=min_samples)
# eps 半径，控制邻域的大小，值越大，越能容忍噪声点，
# 值越小，相比形成的簇就越多
# min_samples 原理中所说的M，控制哪个是核心点，
# 值越小，越可以容忍噪声点，越大，就更容易把有效点划分成噪声点

model.fit(X)
y_hat = model.labels_

unique_y_hat = np.unique(y_hat)
# 获取类簇数 去除离群点-1
n_clusters = len(unique_y_hat) - (1 if -1 in y_hat else 0)
print("类别:", unique_y_hat, "；聚类簇数目:", n_clusters)

def expandBorder(a, b):
    d = (b - a) * 0.1
    return a-d, b+d

x1_min, x2_min = np.min(X, axis=0)
x1_max, x2_max = np.max(X, axis=0)
x1_min, x1_max = expandBorder(x1_min, x1_max)
x2_min, x2_max = expandBorder(x2_min, x2_max)

# 绘图
colors = ['r', 'g', 'b', 'y', 'c', 'k','m','w']

# 区分核心对象
core_samples_mask = np.zeros_like(y_hat, dtype=bool)
core_samples_mask[model.core_sample_indices_] = True

plt.figure(figsize=(12, 8), facecolor='w')
plt.suptitle(u'DBSCAN聚类-数据', fontsize=20)
plt.subplots_adjust(top=0.9,hspace=0.35)
## 开始画图
for k, col in zip(unique_y_hat, colors):
    print(k,col)
    if k == -1:
        col = 'k'

    class_member_mask = (y_hat == k)
    xy = X[class_member_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)

plt.xlim((x1_min, x1_max))
plt.ylim((x2_min, x2_max))
plt.grid(True)
plt.title('$\epsilon$ = %.1f  m = %d，聚类簇数目：%d' % (eps, min_samples,
                                                       n_clusters), fontsize=16)
plt.show()



