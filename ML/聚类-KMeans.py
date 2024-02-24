# -*- coding: utf-8 -*-

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
#自己创建数据库
x,y = make_blobs(n_samples = 500,n_features = 2,centers = 4,random_state = 1)
# print(x)
# fig, ax1 = plt.subplots(1)
# ax1.scatter(x[:,0],x[:,1]
#            ,marker = 'o'#点的形状
#            ,s = 8#点的大小
#            )
# plt.show()

from sklearn.cluster import KMeans
n_clusters = 3
cluster = KMeans(n_clusters = n_clusters, random_state = 0).fit(x)
#重要属性labels_，查看聚好的类别，每个样本所对应的类
y_pred = cluster.labels_
print(y_pred)
print(y_pred==0)
#KMeans因为并不需要建立模型或者预测结果，因此只需要fit就能够得到聚类结果
#KMeans也有接口predict和fit_predict，表示学习数据X并对X的类进行预测
#但所得到的的结果和不调用predict直接fit之后调用属性labels一模一样
pre = cluster.fit_predict(x)
pre == y_pred
#什么时候需要predict呢？当数据量太大的时候
#其实不必使用所有的数据来寻找质心，少量的数据就可以帮助我们确定质心
#当数据量非常大的时候，可以使用部分数据来确定质心
#剩下的数据的聚类结果，使用predict来调用
cluster_smallsub = KMeans(n_clusters = n_clusters,random_state = 0).fit(x[:200])
y_pred_ = cluster_smallsub.predict(x)
y_pred_ == y_pred
#但这样的结果肯定与直接fit全部数据会不一致。当不要求那么精确，或者数据量实在太大，那么可以使用这样的方法。
#重要属性cluster_centers_，查看质心
centroid = cluster.cluster_centers_
centroid
#结果：array([[-7.09306648, -8.10994454],
#            [-1.54234022,  4.43517599],
#            [-8.0862351 , -3.5179868 ]])
centroid.shape
#结果：(3, 2)
#重要属性inertia_，查看总距离平方和
inertia = cluster.inertia_
inertia
#结果：1903.4503741659241
color = ["red","pink","orange","gray"]
# print(x)
# fig,ax1 = plt.subplots(1)
# for i in range(n_clusters):
#     ax1.scatter(x[y_pred == i,0],x[y_pred == i,1]
#                ,marker = "o"
#                ,s = 8
#                ,c = color[i]
#                )
# ax1.scatter(centroid[:,0],centroid[:,1]
#            ,marker = "x"
#            ,s = 15
#            ,c = "black")
# plt.show()