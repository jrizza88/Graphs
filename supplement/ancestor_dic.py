def getParents(ancestors, child):
    parents = []
    for parent_child in ancestors:
        if parent_child[1] == child:
            parents.append(parent_child[0])

    return parents

def dft_recursive(ancestors, node, distances):
    parents = getParents(ancestors, node)
    for parent in parents:
        distances[parent] = distances[node] + 1
        dft_recursive(ancestors, parent, distances)

def earliest_ancestor(ancestors, starting_node):
    distances = {starting_node: 0}
    dft_recursive(ancestors, starting_node, distances)
    grandmost = (starting_node, 0)
    for key, value in distances.items():
        if value > grandmost[1]:
            grandmost = (key, value)
        elif value == grandmost[1]:
            if key < grandmost[0]:
                grandmost = (key, value)
    if grandmost[0] == starting_node:
        return -1
    return grandmost[0]