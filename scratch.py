import pandas as pd
import numpy as np
import scanpy as sc
from ast import literal_eval as make_tuple

early_dir = 'early_vs_terminal/'
dir = 'first_pass_results/'

early_cutoff = 25

f = open(early_dir + 'names.txt', 'r')
early_names = f.read().splitlines()
early_names = [make_tuple(i) for i in early_names]
early_names = early_names[:early_cutoff] + early_names[-early_cutoff:]
expressed_early = [i[0] for i in early_names]
expressed_late = [i[1] for i in early_names]
f.close()

cutoff = 500
f = open(dir + 'names.txt', 'r')
names = f.read().splitlines()
names = [make_tuple(i) for i in names]
names = names[:cutoff] + names[-cutoff:]
f.close()

names = [i for i in names if i[1] not in expressed_late]
names = names[:len(names)//2]

with open('results_8_26.txt', 'w') as f:
    for item in names:
        f.write('%s\n' % str(item))
    
    f.close()
