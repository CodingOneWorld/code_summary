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

# 构建多层感知机,预测Cora数据集分类
'''
https://blog.csdn.net/LOVEmy134611/article/details/137094747
'''

# 多层感知机
class MLP(torch.nn.Module):
    def __init__(self, dim_in, dim_h, dim_out):
        super().__init__()
        self.linear1 = Linear(dim_in, dim_h)
        self.linear2 = Linear(dim_h, dim_out)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.relu(x)
        x = self.linear2(x)
        return F.log_softmax(x, dim=1)

    def fit(self, data, epochs):
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(self.parameters(),
                                     lr=0.01,
                                     weight_decay=5e-4)

        self.train()
        for epoch in range(epochs + 1):
            optimizer.zero_grad()
            out = self(data.x)
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
    def test(self,data):
        self.eval()
        out = self(data.x)
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

    # 传统神经网络-多层感知机 执行分类  只使用节点的特征
    df_x = pd.DataFrame(data.x.numpy())
    df_x['label'] = pd.DataFrame(data.y)
    print(df_x.head())

    mlp = MLP(dataset.num_features, 16, dataset.num_classes)
    print(mlp)

    mlp.fit(data, epochs=100)

    acc = mlp.test(data)
    print(f'\nMLP test accuracy: {acc * 100:.2f}%')




