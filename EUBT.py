def eubt(input_data):

    #Extracting three initial values from the input_data
    x, y, z = input_data.pop(), input_data.pop(), input_data.pop()

    #Creating a set to store unique elements and a set to store trees with the initial values
    exist = {x, y}
    tree_set = {'({},{}),{}'.format(x, y, z)}

    while input_data:

        extra_value, coll = input_data.pop(), set() # Pop the next value from input_data and initialize an empty set for the new trees

        for tree in tree_set:
            for e in exist:
                coll.add(tree.replace(e, '({},{})'.format(e, extra_value)))

            for a, b in enumerate(tree):
                if b != '(':
                    continue
                count = 0

                for i in range(a, len(tree)):
                    if tree[i] == '(':
                        count += 1
                    elif tree[i] == ')':
                        count -= 1
                        if not count:
                            coll.add(tree.replace(tree[a:i+1], '({},{})'.format(tree[a:i+1], extra_value)))
                            break
                        
        exist.add(extra_value)
        tree_set = coll

    #Added a semicolon to each tree 
    tree_set = {'({});'.format(k) for k in tree_set}
    return tree_set

if __name__ == '__main__':
    with open('rosalind_eubt.txt', 'r') as handle:
        taxas_ = handle.read().split()
    with open('output_eubt.txt', 'w') as f:
        print(*eubt(taxas_), sep='\n', file=f)