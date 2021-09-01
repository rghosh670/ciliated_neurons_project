import pandas as pd
import numpy as np
import scanpy as sc

group = 'asymmetric'
output_dir = 'first_pass_results/'

sc._settings.ScanpyConfig.n_jobs = 30

f = open('asymmetric/asymmetric' + '.txt', 'r')
asymmetric = f.read().splitlines()
f.close()

f = open('symmetric/symmetric' + '.txt', 'r')
symmetric = f.read().splitlines()
f.close()

sc.settings.verbosity = 1 

adata = sc.read_csv('transposed_eset.csv',first_column_names=True)

sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

adata.obs['groups'] = ['assymetric' if i in asymmetric else 'symmetric' for i in adata.obs.index.tolist()]

sc.tl.rank_genes_groups(adata, groupby='groups')
# sc.pl.rank_genes_groups(adata)
adata.uns['rank_genes_groups']['names'].tofile(output_dir + 'names.txt', sep='\n')
adata.uns['rank_genes_groups']['scores'].tofile(output_dir + 'scores.txt', sep='\n')
adata.uns['rank_genes_groups']['pvals'].tofile(output_dir + 'pvals.txt', sep='\n')