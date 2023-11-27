#note: we need to reverse the sequence first and then check if the complement of that sequence is equal to the original one

fasta_input = '''>Rosalind_4189
ATATTTTCGCATACAGTCCGTCCTTCGACCCGTATAATTGGTCGTTCGCCCGAGGAGTTT
GTCCCGCAGTAAACAACACATTACATTTTACTCACACCCAGAACTTGCTTGGCGCATAGC
TATAGAACTACAACTCAGGATGTTCTGAGGTATAGGCCGCAGAGCGTATAGATGCGCAAC
GGGGGGTCGAATTGTGAGAGTCTTAAACAACGTTTCTCACAACTAAGTAGCTGCTCCACG
CAGCAGGACGTACTCGCTCAGGGAATGCACAATTCCTACTTCTAAAACGCCGCTATGTAC
TATGTGTGGATGCCGCCGCGAATGCAAAGCAAACATAGTTGTCAACAGTGTCTCTAAAAC
CCCAAACTGGATGGTCACAGACGACTCGACGGATGGCAGCCTAGCTCACAAGAATGATAG
TGAAACAGCAATGTCACGGGGAAGTTAGAATTTCTCATGTCTAGACATTAGTTCAGTTTT
ACATGGCCGAGCGTCGGTGTTGTCAGTCTCCTTGTCACATTTAAAAGCTTAGCAACATAT
TGAAACGTGATACTCTGATAGCCATTAACTACGGCCGTGTGGCTTCCGTGCCCCGTGTGC
GTTGCGAATTGTGTTTAGATTTAAGGTAGGGGTATTAACTACATTGAGATAAGCTATACC
GCTCGTTAGTCAGGGATCTGTTCCGGGTTAGATATAATTGCCGATTCCTCCCCCACCTCG
ATTCCTCGTGGACCTAAGGGGGATCGAGCCGAAGGGCTACCGCAGCTGTAATTAGTGCCA
AGCGCGAGCGTAATTGTTACCATGGGTTCGTGATGCAGGAGGCCCGCAATGCTCACGAAG
TCCATGTTGCTGGGGGAGATTATCATTGTTTATGGTCTTGCTTCTGTCGCACATCTGGGC
CTTTGCTTTCAGGGAATCAAGCGC'''

sequences = fasta_input.split('>')
seq_list = ''

for seq in sequences:
    if seq:
        a = seq.split('\n')
        DNAseq = ''.join(a[1:])
        seq_list += DNAseq

dict_nucl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Reversed seq
def rev_seq(seq):
    new_seq = ''
    new_seq += seq[::-1]
    return new_seq

for i in range(0, len(seq_list)):
    for j in range(4, 13):
        if i + j <= len(seq_list):
            subsequence = seq_list[i:i+j]
            reversed_subsequence = rev_seq(subsequence) #reversing the seq      
            compl_subseq = ''
            for nuc in reversed_subsequence:
                compl_subseq += dict_nucl[nuc]
            if subsequence == compl_subseq: #checking if the compl and the original correspond
                print(i + 1, j)
