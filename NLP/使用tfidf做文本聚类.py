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
        # if r not in stop_words_set:
            result_list.append(r)
    return result_list


def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


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

    # tfidf
    # 将文本中的词语转换为词频矩阵
    # vectorizer = CountVectorizer(analyzer='word', token_pattern=u"(?us).*", stop_words=None)
    vectorizer = CountVectorizer(analyzer='word', token_pattern=u"(?u)\\b\\w+\\b", stop_words=None)
    # 计算个词语出现的次数
    X = vectorizer.fit_transform(reviewArray)
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
    clusters = DBSCAN(eps=0.8, min_samples=3).fit_predict(tfidf.toarray())
    # print(clusters)

    # 生成聚类用户组
    clusters_num = len(np.unique(clusters)) - (1 if -1 in clusters else 0)
