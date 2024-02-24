# -*- coding: utf-8 -*-
import time

import jieba
import jieba.analyse
import re

# 数据预处理
def preHandel(path):
    st = time.time()
    num = 0

    sentences = []

    with open(path) as f:
        for line in f.readlines():
            if line.strip() != "":
                # `[^\w\s]` 匹配除了字母、数字和空格之外的所有字符
                content = re.sub('[^\w\s]', '', line.strip())
                # jieba 分词获取词语序列
                content_seq = list(jieba.cut(content))
                sentences.append(content_seq)

                num += 1

    end = time.time()
    print("PreHandel End Num:%s Cost:%ss" % (num, (end - st)))
    return sentences


# 寻找topN相似
def getSimilarSeq(key, model, top=10):
    print("Top For %s ======================" % key)
    sims = model.wv.most_similar(key, topn=top)
    for i in sims:
        print(i)
    print("End Sim For %s ======================" % key)



if __name__ == '__main__':
    # 1.数据预处理
    path = "./document.txt"
    sentences = preHandel(path)

    for line in sentences:
        print(line)

    from gensim.models import word2vec

    '''
    根据上面的参数介绍传入参数与分词得到的 sentences 序列即可训练得到 w2v 模型，大家可以根据实际情况调整参数，想要增加单词表达能力就
    提高 vector_size，想要快速训练就选择 CBOW 并增加 workers 大小
    '''
    w2v = word2vec.Word2Vec(sentences, hs=1, sg=1, min_count=1, window=5, vector_size=300, workers=4)

    getSimilarSeq("刘备", w2v)
    getSimilarSeq("张飞", w2v)

    # - 寻找不合群单词
    #
    # 给定多个关键词，找出与其他词最不关联的词
    print(w2v.wv.doesnt_match("刘备 张飞 关羽 玄德".split()))


    # 模型与向量存取
    # 存储向量
    from gensim.models import word2vec, KeyedVectors

    word_vectors = w2v.wv
    word_vectors.save("./word2vec.wordvectors")
    wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')
    vector = wv['张飞']
    print(vector)

    # 存储模型
    from gensim.models import Word2Vec
    w2v.save("./w2v.model")
    reloadW2V = Word2Vec.load('./w2v.model')





