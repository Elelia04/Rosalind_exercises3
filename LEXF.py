from itertools import product

def lexf(input_ros):

    input_ros = input_ros.split('\n')
    a = input_ros[0]
    num = int(input_ros[1])

    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    a = a.split(' ')
    
    reordered_seq = sorted(a)

    #generating all the possible combinations
    n_comb = product(reordered_seq, repeat = num)
    for i in list(n_comb):
        a = ''.join(i)
        print(a)
        
input_ros = '''A B C D E F G
3'''

lexf(input_ros)