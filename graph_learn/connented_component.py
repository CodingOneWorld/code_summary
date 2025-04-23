# 连通图挖掘

import networkx as nx
import numpy as np
import pandas as pd

edges_ls=[['A', 'B'],
           ['B', 'D'],
           ['C', 'F']]

g = nx.Graph()
g.add_edges_from(edges_ls)
print('nodes:')
print(g.number_of_nodes())
print('edges:')
print(g.number_of_edges())

# 生成各个连通分量的子图  统计异常节点数
filtered_graphs = []
graphs = [g.subgraph(c).copy() for c in nx.connected_components(g)]
nodes_num = 0
for graph in graphs:
    if graph.number_of_nodes() > 2:
        nodes_num += graph.number_of_nodes()
        filtered_graphs.append(graph)
print('abn_nodes_num:', nodes_num)

# 提取异常的uid和did
# 输出团伙成员
abn_gid_list = []
abn_vid_list = []
group_mems_info=[]
index = 0
for graph in filtered_graphs:
    nodes = graph.nodes
    group_size = len(nodes)
    for node in nodes:
        #         print(node)
        if any(c.isalpha() for c in str(node)):
            #             print(node)
            abn_gid_list.append(node)
            group_mems_info.append([index, node, 'global_id', group_size])
        else:
            abn_vid_list.append(node)
            group_mems_info.append([index, node, 'visitor_id', group_size])
    index += 1
print('团伙gid总数:', len(abn_gid_list))
print('团伙vid总数:', len(abn_vid_list))

# 生成团伙df
group_df = pd.DataFrame(group_mems_info, columns=['group_id', 'node', 'node_type', 'group_size'])
group_df_vid = group_df[group_df.node_type == 'visitor_id']
group_df_vid['node'] = group_df_vid['node'].astype('int')
group_df_vid['node_type'] = group_df_vid['node_type'].astype('str')