# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from gensim.models import word2vec

'''
https://blog.csdn.net/LOVEmy134611/article/details/136355353
'''


# karateclub包实现
def karateclub_DeepWalk(G):
    from karateclub import DeepWalk
    from karateclub import Estimator

    # 初始化DeepWalk模型
    # 模型参数
    #     walk_number（int）：随机行走的次数。默认值为10。
    #     walk_length（int）：随机行走的长度。默认值为80。
    #     dimensions（int）：嵌入的维数。默认值为128。
    #     workers（int）：核心数。默认值为4。
    #     window_size（int）：矩阵幂序。默认值为5。
    #     epochs（int）：迭代次数。默认值为1。
    #     use_hierarchical_softmax（bool）：是使用分层softmax还是负采样来训练模型。默认值为True。
    #     number_of_onegative_samples（int）：要采样的负节点数（通常在5-20之间）。如果设置为0，则不使用负采样。默认值为5。
    #     learning_rate（float）：学习率。默认值为0.05。
    #     min_count（int）：节点出现次数的最小值。默认值为1。
    #     seed（int）：随机种子值。默认值为42
    deepwalk = DeepWalk(walk_number=10, walk_length=80, dimensions=64, epochs=10)

    # 训练模型
    deepwalk.fit(G)

    # 获取嵌入
    embedding = deepwalk.get_embedding()
    print(embedding[0])

# networkx+word2vec实现
# 随机游走函数
def random_walk(start, length):
    walk = [str(start)]  # starting node

    for i in range(length):
        neighbors = [node for node in G.neighbors(start)]
        next_node = np.random.choice(neighbors, 1)[0]
        walk.append(str(next_node))
        start = next_node

    return walk


# 空手道俱乐部内部的关系图。这是一种社交网络，其中的每个节点都是一个成员，而在俱乐部之外进行互动的成员则被连接在一起。
# 在本例中，俱乐部被分为两组：我们希望通过查看每个成员的连接，将每个成员分配到正确的组中(即节点分类，node classification)
def networkx_word2vec_deepwalk(G):
    labels = []
    for node in G.nodes:
        label = G.nodes[node]['club']
        labels.append(1 if label == 'Officer' else 0)

    plt.axis('off')
    nx.draw_networkx(G, pos=nx.spring_layout(G, seed=0), node_color=labels)
    plt.show()

    walks = []
    for node in G.nodes:
        for _ in range(80):
            walks.append(random_walk(node, 10))
    print(walks[0])
    # ['0', '1', '30', '1', '3', '12', '3', '7', '3', '0', '17']

    model = word2vec.Word2Vec(walks,
                     hs=1,  # Hierarchical softmax
                     sg=1,  # Skip-gram
                     vector_size=100,
                     window=10,
                     workers=1)

    # Build vocabulary
    model.build_vocab(walks)
    # Train model
    model.train(walks, total_examples=model.corpus_count, epochs=30, report_delay=1)
    # 查找与给定节点最相似的节点(根据余弦相似度)
    print('Nodes that are the most similar to node 0:')
    for similarity in model.wv.most_similar(positive=['0']):
        print(f'   {similarity}')
    # 输出节点相似度得分
    print(f"\nSimilarity between node 0 and 4: {model.wv.similarity('0', '4')}")
    # Similarity between node 0 and 4: 0.6553224921226501

    # 提取向量表示
    nodes_wv = np.array([model.wv.get_vector(str(i)) for i in range(len(model.wv))])


if __name__ == '__main__':
    # 创建或加载一个图
    G = nx.karate_club_graph()
    print(G.nodes)
    print(G.edges)

    # nx.draw_networkx(G)
    # plt.show()

    # karateclub_DeepWalk(G)




