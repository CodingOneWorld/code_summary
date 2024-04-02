# -*- coding: utf-8 -*-
'''
networkx 文档
https://networkx.org/documentation/latest/reference/index.html
'''

import networkx as nx
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # 无向图
    G = nx.Graph()
    G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    nx.draw_networkx(G)
    plt.show()

    # 有向图
    DG = nx.DiGraph()
    DG.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    nx.draw_networkx(DG)
    plt.show()

    # 加权图
    # 在 networkx 中，图的边用一个包含起点和终点节点的元组以及一个指定边权重的字典来定义的
    WG = nx.Graph()
    WG.add_edges_from([('A', 'B', {"weight": 10}), ('A', 'C', {"weight": 20}),
                       ('B', 'D', {"weight": 30}), ('B', 'E', {"weight": 40}),
                       ('C', 'F', {"weight": 50}), ('C', 'G', {"weight": 60})])
    labels = nx.get_edge_attributes(WG, 'weight')
    nx.draw_networkx(WG)
    nx.draw_networkx_edge_labels(WG, pos=nx.spring_layout(WG), edge_labels=labels)
    plt.show()

    # 简化加权图
    WG = nx.Graph()
    edges=[['A', 'B',1],
           ['B', 'D',2],
           ['C', 'F',3]]
    G.add_weighted_edges_from(edges)
    print('nodes:')
    print(G.number_of_nodes())
    print('edges:')
    print(G.number_of_edges())

    # 入度 出度
    G = nx.Graph()
    G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    print(f"deg(A) = {G.degree['A']}")
    DG = nx.DiGraph()
    DG.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    print(f"deg^-(A) = {DG.in_degree['A']}")
    print(f"deg^+(A) = {DG.out_degree['A']}")













