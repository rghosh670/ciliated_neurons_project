import pandas as pd
import numpy as np
import scanpy as sc

output_dir = 'early_vs_terminal/'

sc._settings.ScanpyConfig.n_jobs = 30

f = open('neuroblasts_and_parents' + '.txt', 'r')
early = f.read().splitlines()
f.close()

f = open('terminal' + '.txt', 'r')
terminal = f.read().splitlines()
f.close()

sc.settings.verbosity = 3 

adata = sc.read_csv('early_vs_terminal/early_vs_terminal_eset.csv',first_column_names=True)

sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

adata.obs['groups'] = ['early' if i in early else 'terminal' for i in adata.obs.index.tolist()]

sc.tl.rank_genes_groups(adata, groupby='groups')
# sc.pl.rank_genes_groups(adata)
adata.uns['rank_genes_groups']['names'].tofile(output_dir + 'names.txt', sep='\n')
adata.uns['rank_genes_groups']['scores'].tofile(output_dir + 'scores.txt', sep='\n')
adata.uns['rank_genes_groups']['pvals'].tofile(output_dir + 'pvals.txt', sep='\n')