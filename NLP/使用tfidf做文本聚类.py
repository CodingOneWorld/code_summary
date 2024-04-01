# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
import jieba
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def del_stop_words(review, stop_words_set):
    #   返回的是去除停用词后的剩余词
    # 去除emoji
    review = filter_emoji(review)
    # 去除标点符号
    words = re.sub('\W*', '', review)
    result_list = []
    result = jieba.cut(words)
    for r in result:
        if r not in stop_words_set:
            result_list.append(r)
    return ','.join(result_list)


def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

# 从文件中读取停用词
def read_from_file(file_name):
    with open(file_name,"r") as fp:
        words = fp.read()
    return words

def get_stop_words(stop_word_file):
    words = read_from_file(stop_word_file)
    result = jieba.cut(words)
    new_words = []
    for r in result:
        new_words.append(r)
    return set(new_words)


if __name__ == '__main__':
    # 导入文本数据
    df = pd.read_csv('review_1441786_202403.csv')
    df = df[['user_id', 'content']]
    print(df.head())
    # 预处理
    df = df.dropna()
    print(df.head())

    stop_words=get_stop_words('stop_words.txt')

    df['content_split'] = df['content'].map(lambda x:del_stop_words(x,stop_words))
    df['con_len'] = df['content'].apply(lambda x: len(x))
    df = df[df.con_len >= 30]
    print(df.head())

    users = df['user_id'].values
    reviews = df['content_split'].values.tolist()
    meta_reviews = df['content'].values.tolist()
    print(reviews[0])
    print('评论数：%d' % (len(reviews)))

    # tfidf
    # 将文本中的词语转换为词频矩阵
    # vectorizer = CountVectorizer(analyzer='word', token_pattern=u"(?us).*", stop_words=None)
    vectorizer = CountVectorizer(analyzer='word', token_pattern=u"(?u)\\b\\w+\\b", stop_words=None)
    # 计算个词语出现的次数
    X = vectorizer.fit_transform(reviews)
    # 获取词袋中所有文本关键词
    word = vectorizer.get_feature_names()
    # print(word)
    # 查看词频结果
    # print(X.toarray())

    # 类调用
    transformer = TfidfTransformer()
    # print(transformer)
    # 将词频矩阵X统计成TF-IDF值
    tfidf = transformer.fit_transform(X)
    # 查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
    # print(tfidf.toarray())
    # 聚类算法
    y_hat = DBSCAN(eps=0.8, min_samples=3).fit_predict(tfidf.toarray())
    # print(clusters)

    unique_y_hat = np.unique(y_hat)
    # 获取类簇数 去除离群点-1
    n_clusters = len(unique_y_hat) - (1 if -1 in y_hat else 0)
    print("类别:", unique_y_hat, "；聚类簇数目:", n_clusters)

    # 输出聚类的评论文本
    clusters_res = [[] for i in range(n_clusters)]
    for idx, c_idx in enumerate(y_hat):
        clusters_res[c_idx].append(meta_reviews[idx])

    for c in clusters_res[:1]:
        print(len(c))
        for r in c:
            print(r)
        print('--------------------------------')



