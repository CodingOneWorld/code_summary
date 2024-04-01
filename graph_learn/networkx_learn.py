# -*- coding: utf-8 -*-
'''
networkx 文档
https://networkx.org/documentation/latest/reference/index.html
'''

import networkx as nx



# 利用networks构建图模型
def createGraph(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    print('nodes:')
    print(G.number_of_nodes())
    print('edges:')
    print(G.number_of_edges())
    return G

if __name__ == '__main__':
    edges=[['a','b',1],
           ['a', 'c', 2],
           ['a', 'd', 3],
           ['a', 'e', 4]]

    graph=createGraph(edges)
    print(graph.degree)




