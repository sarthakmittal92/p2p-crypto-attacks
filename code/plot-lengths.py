import matplotlib.pyplot as plt
from sys import argv
import os
import pathlib
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-mode', '--mode', type = str, help = 'selfish/stubborn', default='selfish')
args = parser.parse_args()
mode = args.mode

directory = "./data"
plots_dir = "./plots"
pathlib.Path(plots_dir).mkdir(exist_ok=True)

mean_lens = {}

for dir in os.listdir(directory):
    j = int(dir)
    filename = os.path.join(directory, dir, f'{mode}-lengths.txt')

    if os.path.isfile(filename):
        with open(filename, 'r' , encoding='utf-8') as f:
            sum_len = 0
            cnt = 0
            for line in f:
                sum_len += int(line.strip())
                cnt += 1
            mean_lens[int(dir)] = (sum_len/cnt)

mean_lens = dict(sorted(mean_lens.items()))

fig, ax = plt.subplots()

ax.scatter(mean_lens.keys(), mean_lens.values(), edgecolors='b', facecolors='none')

l = list(mean_lens.keys())

ax.set_xticks(l)

ax.set_xlabel('Experiment Number')
ax.set_ylabel('Mean branch length')

ax.set_title('Mean Branch Lengths')

fig.set_size_inches(15, 8)

# plt.show()
fig.savefig(os.path.join(plots_dir, f'{mode}-lengths.png'), bbox_inches="tight")
