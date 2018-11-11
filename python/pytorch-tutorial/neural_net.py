import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# nn.Module - encapsulate parameters
# nn.Module will be using autograd
# nn.Module contains layer, forward(input)
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channel, 5x5 square conv
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)

        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        print(x.shape)
        # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2,2))
        print(x.shape)
        # If the size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        print(x.shape)
        x = x.view(-1, self.num_flat_features(x))  # <-- flatten
        print(x.shape)
        x = F.relu(self.fc1(x))
        print(x.shape)
        x = F.relu(self.fc2(x))
        print(x.shape)
        x = self.fc3(x)
        print(x.shape)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s

        return num_features

net = Net()
print(net)

params = list(net.parameters())
print(len(params))
print(params[0].size())

# random input
# batch x channel x width x height
input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)

net.zero_grad()
out.backward(torch.randn(1, 10))

output = net(input)
target = torch.arange(1, 11, dtype=torch.float)  # dummy target [10]
target = target.view(1, -1)  # make it the same shape as output [1, 10]
criterion = nn.MSELoss()  # mean-squared error loss function (평균 제곱 오차)

loss = criterion(output, target)
print(loss)
print(loss.grad_fn)  # MSE Loss
print(loss.grad_fn.next_functions[0][0])  # MSE Loss
print(loss.grad_fn.next_functions[0][0].next_functions[0][0])  # MSE Loss


# Backprop
net.zero_grad()  # clear existing diff. 기존의 변화도를 지우지 않으면 역전파시 기존의 것이 누적된다.

print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)

loss.backward()

print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)


# Optimizer, Update the weights
learning_rate = 0.01
for f in net.parameters():
    f.data.sub_(f.grad.data * learning_rate)


optimizer = optim.SGD(net.parameters(), lr=0.01)

optimizer.zero_grad()  # <-- caution! 
output = net(input)
loss = criterion(output, target)
loss.backward()
optimizer.step()
