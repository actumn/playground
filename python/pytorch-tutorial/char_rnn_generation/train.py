from __future__ import unicode_literals, print_function, division
from io import open
import glob
import unicodedata
import string
import random
import time
import math
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torch.autograd import Variable
from model import RNN


all_letters = string.ascii_letters + " .,;'-"
n_letters = len(all_letters) + 1  # Plus EOS marker


def find_files(path):
    return glob.glob(path)


# Turn a Unicode string to plain ASCII, thanks to http://stackoverflow.com/a/518232/2809427
def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn' and c in all_letters
    )


def read_lines(filename):
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    return [unicode_to_ascii(line) for line in lines]


category_lines = {}
all_categories = []
for filename in find_files('data/names/*txt'):
    category = filename.split('/')[-1].split('.')[0]
    all_categories.append(category)
    lines = read_lines(filename)
    category_lines[category] = lines

n_categories = len(all_categories)

print(f'# categories: {n_categories} {all_categories}')
print(unicode_to_ascii("O'Néàl"))


######################################################################
# For each timestep (that is, for each letter in a training word) the
# inputs of the network will be
# ``(category, current letter, hidden state)`` and the outputs will be
# ``(next letter, next hidden state)``. So for each training set, we'll
# need the category, a set of input letters, and a set of output/target
# letters.
#
# Since we are predicting the next letter from the current letter for each
# timestep, the letter pairs are groups of consecutive letters from the
# line - e.g. for ``"ABCD<EOS>"`` we would create ("A", "B"), ("B", "C"),
# ("C", "D"), ("D", "EOS").
#
# .. figure:: https://i.imgur.com/JH58tXY.png
#    :alt:
#
# The category tensor is a `one-hot
# tensor <https://en.wikipedia.org/wiki/One-hot>`__ of size
# ``<1 x n_categories>``. When training we feed it to the network at every
# timestep - this is a design choice, it could have been included as part
# of initial hidden state or some other strategy.
#

# one hot vector for category
def category_tensor(category):
    li = all_categories.index(category)
    tensor = torch.zeros(1, n_categories)
    tensor[0][li] = 1
    return tensor


# one hot matrix of first to last letters for input
def input_tensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li in range(len(line)):
        letter = line[li]
        tensor[li][0][all_letters.find(letter)] = 1
    return tensor


# long tensor of second letter to end (EOS) for target
def target_tensor(line):
    letter_indexes = [all_letters.find(line[li]) for li in range(1, len(line))]
    letter_indexes.append(n_letters - 1)  # EOS
    return torch.LongTensor(letter_indexes)


######################################################################
# Training
# =========
# Preparing for Training
# ----------------------
#
# First of all, helper functions to get random pairs of (category, line):
#

# random from list
def random_choice(l):
    return l[random.randint(0, len(l) - 1)]


# random category and random line from that category
def random_training_pair():
    category = random_choice(all_categories)
    return category, random_choice(category_lines[category])


######################################################################
# For convenience during training we'll make a ``random_training_example``
# function that fetches a random (category, line) pair and turns them into
# the required (category, input, target) tensors.
#

# Make category, input, and target tensors from a random category, line pair
def random_training_example():
    category, line = random_training_pair()
    return category_tensor(category), input_tensor(line), target_tensor(line)


######################################################################
# To keep track of how long training takes I am adding a
# ``timeSince(timestamp)`` function which returns a human readable string:
#

def time_since(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return f'{m} {s}'


######################################################################
# Training the Network
# --------------------
#
# In contrast to classification, where only the last output is used, we
# are making a prediction at every step, so we are calculating loss at
# every step.
#
# The magic of autograd allows you to simply sum these losses at each step
# and call backward at the end.
#

criterion = nn.NLLLoss()
learning_rate = 0.0005

rnn = RNN(n_letters, 128, n_letters, n_categories=n_categories)


def train(category_tensor_variable, input_line_tensor, target_line_tensor):
    hidden = rnn.init_hidden()
    rnn.zero_grad()

    loss = 0

    for i in range(input_line_tensor.size(0)):
        output, hidden = rnn(category_tensor_variable, input_line_tensor[i], hidden)
        print(input_line_tensor.size())
        print(output.size())
        print(target_line_tensor[i])
        loss += criterion(output, target_line_tensor[i])

    loss.backward()

    for p in rnn.parameters():
        p.data.add_(-learning_rate, p.grad.data)

    return output, loss.data[0] / input_line_tensor.size()[0]


n_iters = 100 * 1000
print_every = 5000
plot_every = 500
all_losses = []
total_loss = 0  # Reset every plot_every iters

start = time.time()

for iter in range(1, n_iters + 1):
    output, loss = train(*random_training_example())
    total_loss += loss

    if iter % print_every == 0:
        print(f'{time_since(start)} ({iter}, {iter / n_iters * 100}%%) {loss}')

    if iter % plot_every == 0:
        all_losses.append(total_loss / plot_every)
        total_loss = 0


######################################################################
# Plotting the Losses
# -------------------
#
# Plotting the historical loss from all\_losses shows the network
# learning:
#
plt.figure()
plt.plot(all_losses)


######################################################################
# Sampling the Network
# ====================
#
# To sample we give the network a letter and ask what the next one is,
# feed that in as the next letter, and repeat until the EOS token.
#
# -  Create tensors for input category, starting letter, and empty hidden
#    state
# -  Create a string ``output_name`` with the starting letter
# -  Up to a maximum output length,
#
#    -  Feed the current letter to the network
#    -  Get the next letter from highest output, and next hidden state
#    -  If the letter is EOS, stop here
#    -  If a regular letter, add to ``output_name`` and continue
#
# -  Return the final name
#
# .. Note::
#    Rather than having to give it a starting letter, another
#    strategy would have been to include a "start of string" token in
#    training and have the network choose its own starting letter.
#

max_length = 20


def sample(category, start_letter='A'):
    category_tensor_variable = Variable(category_tensor(category))
    input = Variable(input_tensor(start_letter))
    hidden = rnn.init_hidden()

    output_name = start_letter

    for i in range(max_length):
        output, hidden = rnn(category_tensor_variable, input[0], hidden)
        topy, topi = output.data.topk(1)
        topi = topi[0][0]

        if topi == n_letters - 1:
            break
        else:
            letter = all_letters[topi]
            output_name += letter

        input = Variable(input_tensor(letter))

    return output_name


# Get multiple samples from one category and multiple starting letters
def samples(category, start_letters='ABC'):
    for start_letter in start_letters:
        print(sample(category, start_letter))


samples('Russian', 'RUS')
samples('German', 'GER')
samples('Spanish', 'SPA')
samples('Chinese', 'CHI')


######################################################################
# Save the model
"""
torch.save(rnn.state_dict(), 'model.pth')

import pickle
to_pickle = {
    'all_categories': all_categories,
    'n_categories': n_categories,
    'all_letters': all_letters,
    'n_letters': n_letters
}
with open('params.pkl', 'wb') as file:
    pickle.dump(to_pickle, file)
"""
