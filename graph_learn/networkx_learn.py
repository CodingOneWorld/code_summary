# -*- coding: utf-8 -*-
'''
networkx 文档
https://networkx.org/documentation/latest/reference/index.html
'''

import networkx as nx
from matplotlib import pyplot as plt
import numpy as np

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
    # 图的属性
    print('nodes:')
    print(G.number_of_nodes())
    print('edges:')
    print(G.number_of_edges())
    # 边集 list
    print(G.edges)
    # 点集 list
    print(G.nodes)
    # 每个节点的度 dict
    print(nx.degree(G))
    # 图的平均度
    # 获取网络的度, 并转为字典类型
    d = dict(nx.degree(G))
    # 计算网络的平均度=节点度之和/结点个数
    # print(d.values())
    d_avg = np.sum(list(d.values())) / len(G.nodes)
    print(d_avg)
    # 图的平均边权重
    # 获取图的邻接矩阵，获取的是边
    As = nx.adjacency_matrix(G)
    # 将边转为二维矩阵
    A = As.todense()
    # 查看邻接矩阵
    # print(A)
    avg_w = np.sum(A) / G.number_of_edges()
    print(avg_w)
    # 平均集聚系数
    print(nx.average_clustering(G))
    # 全局集聚系数
    print(nx.transitivity(G))

    # 入度 出度
    G = nx.Graph()
    G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    print(f"deg(A) = {G.degree['A']}")
    DG = nx.DiGraph()
    DG.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    print(f"deg^-(A) = {DG.in_degree['A']}")
    print(f"deg^+(A) = {DG.out_degree['A']}")















