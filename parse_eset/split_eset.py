import pandas as pd

f = open('asymmetric/asymmetric.txt', 'r')
asymmetric = f.read().splitlines()
f.close()

f = open('symmetric/symmetric.txt', 'r')
symmetric = f.read().splitlines()
f.close()

df = pd.read_csv('transposed_eset.csv', index_col=0)

index = df.index.tolist()

asym_idx = []
sym_idx = []

for i, v in enumerate(index):
    if v in asymmetric:
        asym_idx.append(i)
    elif v in symmetric:
        sym_idx.append(i)

asym_df = df.iloc[asym_idx]
sym_df = df.iloc[sym_idx]

asym_df.to_csv('asymmetric/asymmetric_df.csv')
sym_df.to_csv('symmetric/symmetric_df.csv')





