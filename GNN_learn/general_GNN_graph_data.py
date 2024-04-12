# -*- coding: utf-8 -*-

# 常用的图数据集

import torch
from torch_geometric.datasets import Planetoid


if __name__ == '__main__':
    # cora数据集
    # 使用 Planetoid 类下载数据集
    dataset = Planetoid(root=".", name="Cora")
    # Cora 只有一个图，将其存储在 data 变量中
    data = dataset[0]
    # 打印数据集的相关信息
    print(f'Dataset: {dataset}')
    print('---------------')
    print(f'Number of graphs: {len(dataset)}')
    print(f'Number of nodes: {data.x.shape[0]}')
    print(f'Number of features: {dataset.num_features}')
    print(f'Number of classes: {dataset.num_classes}')
    # 通过 PyTorch Geometric 的专用函数，还可以获得更多详细信息
    # Print information about the graph
    print(f'\nGraph:')
    print('------')
    print(f'Edges are directed: {data.is_directed()}')
    print(f'Graph has isolated nodes: {data.has_isolated_nodes()}')
    print(f'Graph has loops: {data.has_self_loops()}')

    # Facebook Page-Page 数据集
    from torch_geometric.datasets import FacebookPagePage

    dataset = FacebookPagePage(root=".", name="FacebookPagePage")
    data = dataset[0]
    # 打印数据集的相关信息
    print(f'Dataset: {dataset}')
    print('-----------------------')
    print(f'Number of graphs: {len(dataset)}')
    print(f'Number of nodes: {data.x.shape[0]}')
    print(f'Number of features: {dataset.num_features}')
    print(f'Number of classes: {dataset.num_classes}')
    # 更多详细信息
    print(f'\nGraph:')
    print('------')
    print(f'Edges are directed: {data.is_directed()}')
    print(f'Graph has isolated nodes: {data.has_isolated_nodes()}')
    print(f'Graph has loops: {data.has_self_loops()}')








