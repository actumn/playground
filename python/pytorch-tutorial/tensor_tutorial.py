from __future__ import print_function
import torch


# alternatives of numpy, for using GPUs
# Tensors ~= Numpy array
x = torch.empty(5, 3)
print(x)

x = torch.rand(5, 3)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3])
print(x)
print(x.size())

x = x.new_ones(5, 3, dtype=torch.double)
print(x)

x = torch.randn_like(x, dtype=torch.float)
print(x)
print(x.size())

y = torch.rand(5, 3)
print(x+y)
print(torch.add(x, y))

result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)


print(x[:, 1])

# resizing
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)       # -1 is inferred from other dimension
v = x.view(2, 2, -1)
print(x.size(), y.size(), z.size(), v.size())


x = torch.randn(1)
print(x)
print(x.item())


# Numpy Bridge
# torch tensor -> numpy array
a = torch.ones(5)
b = a.numpy()
print(a)
print(b)
a.add_(1)
print(a)
print(b)

# numpy array -> torch tensor
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)


# CUDA TENSOR
if torch.cuda.is_available():
    device = torch.device('cuda')           # CUDA device object
    y = torch.ones_like(x, device=device)   # created a tensor on GPU
    x = x.to(device)
    z = x + y
    print(z)
    print(z.to('cpu', torch.double))
