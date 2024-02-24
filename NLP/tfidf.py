# -*- coding: utf-8 -*-

import re
import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# 过滤表情符号
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



def caltfidf(dataArray):
    reviewArray = []
    # 对每条评论文本预处理
    for line in dataArray:
        review_cut = set(del_stop_words(line[3]))
        review_cut = ",".join(review_cut)
        if len(review_cut) > 10:
            reviewArray.append(review_cut)

    if len(reviewArray)>0:
        # 将文本中的词语转换为词频矩阵
        # vectorizer = CountVectorizer(analyzer='word', token_pattern=u"(?us).*", stop_words=None)
        vectorizer = CountVectorizer(analyzer='word', token_pattern=u"(?u)\\b\\w+\\b", stop_words=None)
        # 计算每个词语出现的次数
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

        return tfidf