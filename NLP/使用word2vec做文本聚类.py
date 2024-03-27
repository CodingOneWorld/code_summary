# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
import jieba
from gensim.models.doc2vec import Doc2Vec, TaggedDocument #导入模型
from sklearn.cluster import DBSCAN

# 显示所有行(参数设置为None代表显示所有行，也可以自行设置数字)
pd.set_option('display.max_columns', None)
# 显示所有列
pd.set_option('display.max_rows', None)
# 设置数据的显示长度，默认为50
pd.set_option('max_colwidth', 2000)
# 禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)

def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

# 删除停用词 如标点符号等
def del_stop_words(review, stop_words_set={}):
    #   返回的是去除停用词后的剩余词
    # 去除emoji
    review = filter_emoji(review)
    # 去除标点符号
    words = re.sub('\W*', '', review)
    result_list = []
    result = jieba.cut(words)
    for r in result:
        # if r not in stop_words_set:
            result_list.append(r)
    return result_list


if __name__ == '__main__':
    # 导入文本数据
    df = pd.read_csv('review_1441786_202403.csv')
    df = df[['user_id', 'content']]
    print(df.head())
    # 预处理
    df = df.dropna()
    print(df.head())

    df['content_split'] = df['content'].apply(del_stop_words)
    df['con_len'] = df['content'].apply(lambda x: len(x))
    df = df[df.con_len >= 30]
    print(df.head())

    users = df['user_id'].values
    reviews = df['content_split'].values
    meta_reviews = df['content'].values
    print('评论数：%d' % (len(reviews)))
    # 向量化 word2vec
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(reviews)]
    model = Doc2Vec(documents, vector_size=100, window=2, min_count=1, workers=4)  # 设置模型参数
    # 获取句向量
    sen_vec = model.dv[[i for i in range(0, len(reviews))]]
    print(sen_vec)
    # 聚类 DBScan
    eps = 0.4
    min_samples = 10
    model = DBSCAN(eps=eps, min_samples=min_samples)
    model.fit(sen_vec)
    y_hat = model.labels_

    unique_y_hat = np.unique(y_hat)
    # 获取类簇数 去除离群点-1
    n_clusters = len(unique_y_hat) - (1 if -1 in y_hat else 0)
    print("类别:", unique_y_hat, "；聚类簇数目:", n_clusters)

    # 输出聚类的评论文本
    clusters = [[] for i in range(n_clusters)]
    for idx, c_idx in enumerate(y_hat):
        clusters[c_idx].append(meta_reviews[idx])

    for c in clusters[:1]:
        print(len(c))
        for r in c:
            print(r)
        print('--------------------------------')
