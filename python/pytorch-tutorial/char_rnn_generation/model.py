# model.py
######################################################################
# Creating the Network
# ====================
#
# This network extends `the last tutorial's RNN <#Creating-the-Network>`__
# with an extra argument for the category tensor, which is concatenated
# along with the others. The category tensor is a one-hot vector just like
# the letter input.
#
# We will interpret the output as the probability of the next letter. When
# sampling, the most likely output letter is used as the next input
# letter.
#
# I added a second linear layer ``o2o`` (after combining hidden and
# output) to give it more muscle to work with. There's also a dropout
# layer, which `randomly zeros parts of its
# input <https://arxiv.org/abs/1207.0580>`__ with a given probability
# (here 0.1) and is usually used to fuzz inputs to prevent overfitting.
# Here we're using it towards the end of the network to purposely add some
# chaos and increase sampling variety.
#
# .. figure:: https://i.imgur.com/jzVrf7f.png
#    :alt:
#
#
import torch
import torch.nn as nn
from torch.autograd import Variable


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_categories):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        print(input_size)
        print(output_size)

        self.i2h = nn.Linear(n_categories + input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(n_categories + input_size + hidden_size, output_size)
        self.o2o = nn.Linear(hidden_size + output_size, output_size)
        self.dropout = nn.Dropout(0.1)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, category, input, hidden):
        input_combined = torch.cat((category, input, hidden), 1)
        hidden = self.i2h(input_combined)
        output = self.i2o(input_combined)
        output_combined = torch.cat((hidden, output), 1)
        output = self.o2o(output_combined)
        output = self.dropout(output)
        output = self.softmax(output)
        return output, hidden

    def init_hidden(self):
        return Variable(torch.zeros(1, self.hidden_size))
