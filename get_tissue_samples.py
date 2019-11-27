import sys

file_name = 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'


def get_counts(tissue_name, gene_name, out_file_name):

    o = open(out_file_name, 'w')

    header = None
    sampid_col = -1
    tissue_col = -1

    f = open(file_name)
    for l in f:
        A = l.rstrip().split('\t')
        if header is None:
            header = A
            sampid_col = A.index('SAMPID')
            tissue_col = A.index(gene_name)
            continue

        if A[tissue_col] == tissue_name:
            o.write(A[sampid_col] + '\n')
    f.close()
    o.close()
