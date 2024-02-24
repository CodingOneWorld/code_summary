# -*- coding: utf-8 -*-

from gensim.test.utils import common_texts #加载语料库

print(common_texts)
'''
common_texts:
[['human', 'interface', 'computer'],
 ['survey', 'user', 'computer', 'system', 'response', 'time'],
 ['eps', 'user', 'interface', 'system'],
 ['system', 'human', 'system', 'eps'],
 ['user', 'response', 'time'],
 ['trees'],
 ['graph', 'trees'],
 ['graph', 'minors', 'trees'],
 ['graph', 'minors', 'survey']]
'''

from gensim.models.doc2vec import Doc2Vec, TaggedDocument #导入模型
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
'''
documents:
[TaggedDocument(words=['human', 'interface', 'computer'], tags=[0]),
 TaggedDocument(words=['survey', 'user', 'computer', 'system', 'response', 'time'], tags=[1]),
 TaggedDocument(words=['eps', 'user', 'interface', 'system'], tags=[2]),
 TaggedDocument(words=['system', 'human', 'system', 'eps'], tags=[3]),
 TaggedDocument(words=['user', 'response', 'time'], tags=[4]),
 TaggedDocument(words=['trees'], tags=[5]),
 TaggedDocument(words=['graph', 'trees'], tags=[6]),
 TaggedDocument(words=['graph', 'minors', 'trees'], tags=[7]),
 TaggedDocument(words=['graph', 'minors', 'survey'], tags=[8])]
'''

model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4) #设置模型参数
'''
documents:训练文档；
dm:定义了训练算法，1：PV-DM模型，0：PV-DBOW，default：1
vector_size：段落向量维度；
window：滑动窗口大小，defaul：5；
min_count：最小词频；
workers：使用多少个线程训练模型；
epochs:训练几轮，default：10；
'''

# 预测新文档的文档向量
vector = model.infer_vector(["system", "response"])
print(vector)

# vector:[ 0.07526284  0.03071802  0.06952841  0.07332748 -0.00398467]
#获取词向量
model.wv["human"]
# array([-0.08951139,  0.09008525, -0.13615547, -0.07095552,  0.18797508],dtype=float32)
#获取句子向量
sen_vec=model.dv[[i for i in range(0,9)]]
print(sen_vec)
# array([[-0.10505038, -0.11994538, -0.1980365 ,  0.17078663,  0.07128712],
#        [ 0.00469663, -0.19779648, -0.10351036, -0.19501851,  0.04011496]],
#       dtype=float32)

# # 保存模型
# model.save("tess.model")
#
# # 模型加载
# from gensim.test.utils import get_tmpfile
#
# fname = get_tmpfile("./tess.model")
# model = Doc2Vec.load(fname)