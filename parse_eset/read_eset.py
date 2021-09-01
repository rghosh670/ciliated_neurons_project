import pandas as pd

group_1 = 'neuroblasts_and_parents'
group_2 = 'terminal'

f = open(group_1 + '.txt', 'r')
group_1_cells = f.read().splitlines()
f.close()

f = open(group_2 + '.txt', 'r')
group_2_cells = f.read().splitlines()
f.close()

cell = pd.read_csv('~/Desktop/cell_subtype.csv', index_col=0)['x'].tolist()

combined = group_1_cells + group_2_cells

cols = cell

cell = [i for i in cell if i in combined]

idx = []

for i, v in enumerate(cols):
    if v in combined:
        idx.append(i+1)

idx.insert(0,0)

df = pd.read_csv('~/Desktop/embryo_eset.csv', index_col=0, usecols=idx)
df.columns = cell
df = df.T
df.to_csv('early_vs_terminal/early_vs_terminal_eset.csv')
