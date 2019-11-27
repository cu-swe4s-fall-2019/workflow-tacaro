import sys
import gzip

file_name = 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.gct'


def get_counts(gene_name, output):

    o = open(output, 'w')

    version = None
    d = None
    hdr = None

    f = open(file_name, 'rt')
    for l in f:
        A = l.rstrip().split('\t')
        if version is None:
            version = A
            continue
        if d is None:
            d = A
            continue
        if hdr is None:
            hdr = A
            continue
        if A[1] == gene_name:
            for i in range(2, len(hdr)):
                o.write(hdr[i] + ' ' + A[i] + '\n')
    f.close()
    o.close()


get_counts('SDHB', 'test.txt')
