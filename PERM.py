from itertools import permutations

n = 4

def perm(n):  
    # initializing a list containing the numbers undergoing permutation 
    lst1 = list(range(n+1))
    lst1.remove(0)

    #Updating the permutations counter
    count = 0 

    # calculating the permutations 
    perm_list = list(permutations(lst1))
    
    with open("permutations.txt", "w") as file:
        for el in perm_list:
            count += 1
        print(count, file=file)
    
        for i in perm_list:
            print(" ".join(map(str, i)), file=file)

perm(n)
