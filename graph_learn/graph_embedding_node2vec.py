# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from gensim.models import word2vec

'''
https://blog.csdn.net/LOVEmy134611/article/details/136359416'''

# 实现有偏随机游走
def next_node(previous, current, p, q):
    # 检索当前节点的邻居节点列表，并初始化 alpha 值列表
    alphas = []
    # Get the neighboring nodes
    neighbors = list(G.neighbors(current))

    # 对于每个邻居，都要计算出相应的 alpha 值：如果该邻居是前一个节点，则为 1/p；如果该邻居与前一个节点相连，则为 1；否则为 1/q
    # Calculate the appropriate alpha value for each neighbor
    for neighbor in neighbors:
        # Distance = 0: probability to return to the previous node
        if neighbor == previous:
            alpha = 1/p
        # Distance = 1: probability of visiting a local node
        elif G.has_edge(neighbor, previous):
            alpha = 1
        # Distance = 2: probability to explore an unknown node
        else:
            alpha = 1/q
        alphas.append(alpha)

    # 对这些值进行归一化处理，得出概率
    probs = [alpha / sum(alphas) for alpha in alphas]

    # 根据上一步计算出的转换概率，使用 np.random.choice() 随机选择下一个节点并返回
    next = np.random.choice(neighbors, size=1, p=probs)[0]
    return next


# 随机游走
def random_walk(start, length, p, q):
    walk = [start]

    for i in range(length):
        current = walk[-1]
        previous = walk[-2] if len(walk) > 1 else None
        next = next_node(previous, current, p, q)
        walk.append(next)

    return walk

# networkx+word2bvec-->node2vec
def networkx_word2vec_node2vec(G):
    # Process labels (Mr. Hi = 0, Officer = 1)
    labels = []
    for node in G.nodes:
        label = G.nodes[node]['club']
        labels.append(1 if label == 'Officer' else 0)

    walks = []
    for node in G.nodes:
        for _ in range(80):
            walks.append(random_walk(node, 10, 3, 2))

    node2vec = word2vec.Word2Vec(walks,
                        hs=1,  # Hierarchical softmax
                        sg=1,  # Skip-gram
                        vector_size=100,
                        window=10,
                        workers=2,
                        min_count=1)

    node2vec.train(walks, total_examples=node2vec.corpus_count, epochs=30, report_delay=1)


if __name__ == '__main__':
    # Create graph
    G = nx.erdos_renyi_graph(10, 0.3, seed=1, directed=False)

    # Plot graph
    plt.axis('off')
    nx.draw_networkx(G, pos=nx.spring_layout(G, seed=0))
    # plt.show()

    # test
    print(random_walk(0, 8, p=1, q=1))
    # 接下来，令算法偏向于回到前一个节点，即 q=10
    print(random_walk(0, 8, p=1, q=10))
    # 接下来，使用 p=10 调用函数，由于其概率很低，所以不会返回到之前的节点
    print(random_walk(0, 8, p=10, q=1))






