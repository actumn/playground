import torch

x = torch.ones(2, 2, requires_grad=True)
print(x)
print(x.shape)

y = x + 2
print(y)
print(y.grad_fn)

z = y * y * 3
out = z.mean()
print(z, out)

# z = 3*(x+2)**2
# out = 1/4 * sum(z)
# dout/dx = 3/2 * (x + 2)
out.backward()
print(x.grad)

x = torch.randn(3, requires_grad=True)
y = x * 2
# y.norm = square_root(sum(yi ** 2))
while y.data.norm() < 1000:
    y = y * 2

print(y)

gradients = torch.tensor([0.1, 1.0, 0.001], dtype=torch.float)
y.backward(gradients)
print(x.grad)


# grad_fn : 도함수. 기울기 계산 
a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b = (a * a).sum()
print(b.grad_fn)
