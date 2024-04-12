# -*- coding: utf-8 -*-

import torch
from torch_geometric.datasets import Planetoid
from torch_geometric.utils import degree
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

# 显示所有行(参数设置为None代表显示所有行，也可以自行设置数字)
pd.set_option('display.max_columns', None)
# 显示所有列
pd.set_option('display.max_rows', None)
# 设置数据的显示长度，默认为50
pd.set_option('max_colwidth', 200)
# 禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)

# GCN实现
'''
https://blog.csdn.net/LOVEmy134611/article/details/137302130
'''

# GCN类
class GCN(torch.nn.Module):
    def __init__(self,dim_in,dim_h,dim_out):
        super().__init__()
        self.gcn1=GCNConv(dim_in,dim_h)
        self.gcn2=GCNConv(dim_h,dim_out)

    def forward(self, x, edge_index):
        h = self.gcn1(x, edge_index)
        h = torch.relu(h)
        h = self.gcn2(h, edge_index)
        return F.log_softmax(h, dim=1)


    def fit(self, data, epochs):
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(self.parameters(),
                                      lr=0.01,
                                      weight_decay=5e-4)

        self.train()
        for epoch in range(epochs+1):
            optimizer.zero_grad()
            out = self(data.x, data.edge_index)
            loss = criterion(out[data.train_mask], data.y[data.train_mask])
            acc = accuracy(out[data.train_mask].argmax(dim=1),
                          data.y[data.train_mask])
            loss.backward()
            optimizer.step()

            if(epoch % 20 == 0):
                val_loss = criterion(out[data.val_mask], data.y[data.val_mask])
                val_acc = accuracy(out[data.val_mask].argmax(dim=1),
                                  data.y[data.val_mask])
                print(f'Epoch {epoch:>3} | Train Loss: {loss:.3f} | Train Acc:'
                      f' {acc*100:>5.2f}% | Val Loss: {val_loss:.2f} | '
                      f'Val Acc: {val_acc*100:.2f}%')

    @torch.no_grad()
    def test(self, data):
        self.eval()
        out = self(data.x, data.edge_index)
        acc = accuracy(out.argmax(dim=1)[data.test_mask], data.y[data.test_mask])
        return acc


if __name__ == '__main__':
    # cora图数据集
    dataset = Planetoid(root=".", name="Cora")
    data = dataset[0]
    # 计算图中每个节点的邻居数
    degrees = degree(data.edge_index[0]).numpy()
    print(degrees)
    # 为了生成更自然的可视化效果，统计具有相同度的节点数量
    numbers = Counter(degrees)
    # 使用条形图来绘制统计结果
    fig, ax = plt.subplots()
    ax.set_xlabel('Node degree')
    ax.set_ylabel('Number of nodes')
    plt.bar(numbers.keys(), numbers.values())
    # plt.show()

    # GCN
    import torch.nn.functional as F
    from torch_geometric.nn import GCNConv

    def accuracy(y_pred,y_true):
        """Calculate accuracy."""
        return torch.sum(y_pred==y_true)/len(y_true)


    # 实例化并训练100个epoch
    gcn=GCN(dataset.num_features,16,dataset.num_classes)
    print(gcn)

    # Train
    gcn.fit(data, epochs=100)















