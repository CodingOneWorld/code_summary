# -*- coding: utf-8 -*-

from torch_geometric.datasets import Planetoid
import pandas as pd
import torch
from torch.nn import Linear
import torch.nn.functional as F

# 显示所有行(参数设置为None代表显示所有行，也可以自行设置数字)
pd.set_option('display.max_columns', None)
# 显示所有列
pd.set_option('display.max_rows', None)
# 设置数据的显示长度，默认为50
pd.set_option('max_colwidth', 200)
# 禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)

# MLP+图神经网络
'''
https://blog.csdn.net/LOVEmy134611/article/details/137094747
'''


# 图线性层
class MLPGNNLayer(torch.nn.Module):
    def __init__(self, dim_in, dim_out):
        super().__init__()
        self.linear = Linear(dim_in, dim_out, bias=False)

    # 在forward() 方法中执行两个操作，首先执行线性变换，然后与邻接矩阵A相乘
    def forward(self, x, adjacency):
        x = self.linear(x)
        x = torch.sparse.mm(adjacency, x)
        return x


# 基于图线性层的MLPGNN
class MLPGNN(torch.nn.Module):
    """MLP Graph Neural Network"""
    def __init__(self, dim_in, dim_h, dim_out):
        super().__init__()
        self.gnn1 = MLPGNNLayer(dim_in, dim_h)
        self.gnn2 = MLPGNNLayer(dim_h, dim_out)

    def forward(self, x, adjacency):
        h = self.gnn1(x, adjacency)
        h = torch.relu(h)
        h = self.gnn2(h, adjacency)
        return F.log_softmax(h, dim=1)

    def fit(self, data, epochs):
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(self.parameters(),
                                     lr=0.01,
                                     weight_decay=5e-4)

        self.train()
        for epoch in range(epochs + 1):
            optimizer.zero_grad()
            out = self(data.x, adjacency)
            loss = criterion(out[data.train_mask], data.y[data.train_mask])
            acc = accuracy(out[data.train_mask].argmax(dim=1),
                           data.y[data.train_mask])
            loss.backward()
            optimizer.step()

            if (epoch % 20 == 0):
                val_loss = criterion(out[data.val_mask], data.y[data.val_mask])
                val_acc = accuracy(out[data.val_mask].argmax(dim=1),
                                   data.y[data.val_mask])
                print(f'Epoch {epoch:>3} | Train Loss: {loss:.3f} | Train Acc:'
                      f' {acc * 100:>5.2f}% | Val Loss: {val_loss:.2f} | '
                      f'Val Acc: {val_acc * 100:.2f}%')

    @torch.no_grad()
    def test(self, data):
        self.eval()
        out = self(data.x, adjacency)
        acc = accuracy(out.argmax(dim=1)[data.test_mask], data.y[data.test_mask])
        return acc


# 评估标准
def accuracy(y_pred, y_true):
    """Calculate accuracy."""
    return torch.sum(y_pred == y_true) / len(y_true)


if __name__ == '__main__':
    # 导入图数据
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

    # 根据图的边生成邻接矩阵
    from torch_geometric.utils import to_dense_adj

    adjacency = to_dense_adj(data.edge_index)[0]
    adjacency += torch.eye(len(adjacency))
    print(data.edge_index.shape)
    print(adjacency)

    # 创建、训练并评估模型
    gnn = MLPGNN(dataset.num_features, 16, dataset.num_classes)
    print(gnn)
    # Train
    gnn.fit(data, epochs=100)
    # Test
    acc = gnn.test(data)
    print(f'\nGNN test accuracy: {acc * 100:.2f}%')
