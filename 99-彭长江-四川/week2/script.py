import torch
import numpy as np


x = np.array([[4, 3, 2, 1],
              [1, 2, 3, 4]])
# 矩阵的维度
print(x.ndim)

# 矩阵的形状
print(x.shape)

# 矩阵元素个数
print(x.size)

# 矩阵相加
print(sum(x))
# 矩阵竖着相加    在指定维度操作
print(np.sum(x, axis=0))
# 矩阵横着相加    在指定维度操作
print(np.sum(x, axis=1))

# 矩阵形状变化，变化为4X2
print(np.reshape(x, (4, 2)))

# 开根号
print(np.sqrt(x))

# 指数函数
print(np.exp(x))

# 矩阵旋转
print(x.transpose())

# 将矩阵返回一维
print(x.flatten())

# 生成3个4X5的全零矩阵
print(np.zeros((3, 4, 5)))
# 随机生成3个4X5的矩阵
print(np.random.rand(3, 4, 5))


y = np.random.rand(4, 3, 2)
x = torch.FloatTensor(y)
print(x.shape)
print(torch.exp(x))
print(torch.sum(x, dim=0))
print(torch.sum(x, dim=1))
print(x.transpose(1, 0))
print(x.flatten())

z = torch.nn.BatchNorm1d(10)
torch.nn.BatchNorm2d(10)
torch.nn.BatchNorm3d(10)
print(z.state_dict())
x = torch.rand((2, 10))
print(z(x))
