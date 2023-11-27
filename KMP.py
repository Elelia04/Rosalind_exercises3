from Bio import SeqIO

def kmp_failure_array(sequence):
    failure_array = [0] * len(sequence)

    for length in range(1, len(sequence)):
        current_motif_length = 0  

        # Starting from the smallest motif found, check if, from pos 1, the motif corresponds
        for j in range(1, len(sequence) - length + 1):
            if sequence[:length] == sequence[j:j + length]:
                failure_array[j + length - 1] = len(sequence[:length])
                current_motif_length = len(sequence[:length])

        if current_motif_length < len(sequence[:length]):
            break

    return failure_array

#Opening fasta format
with open("kmp.txt", "r") as f:
    a = SeqIO.read(f, "fasta")
    str1 = str(a.seq)

result = kmp_failure_array(str1)

with open("kmp_result.txt", "w") as output_file:
    output_file.write(' '.join(map(str, result)))

