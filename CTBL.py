import newick

def character_table(in_tree):
    leaves = list(get_lflab(in_tree))
    leaves.sort()

    edges = list(get_edg(in_tree))
    connections = []
    
    for node1, node2 in edges:
        if node1.descendants and node2.descendants:
            char_leaves = set(get_lflab(in_tree, exclude_node=node2))
            connection_str = ''
            for leaf in leaves:
                if leaf in char_leaves:
                    connection_str += '0'
                else:
                    connection_str += '1'
            connections.append(connection_str)

    return '\n'.join(connections)

def get_lflab(node, exclude_node=None): #Getting leaf labels 
    if node is exclude_node:
        return
    if not node.descendants:
        yield node.name  # Using name instead of label
    else:
        for child in node.descendants:
            yield from get_lflab(child, exclude_node)

def get_edg(node):
    for child in node.descendants:
        yield node, child
        yield from get_edg(child)

if __name__ == '__main__':
    with open('rosalind_ctbl.txt') as file:
        
        #Reading the content of the file
        newick_str = file.read().strip()
        in_tree = newick.loads(newick_str)[0]

        result = character_table(in_tree)
        print(result)
