import numpy as np

def MP_root_ete3(my_tree):
    """
    
    """
    init_bl = np.sum([i.dist for i in my_tree.traverse()])
    init_terms = my_tree.get_leaves()
    init_term_names = [i.name for i in my_tree.get_leaves()]
    if len(my_tree.children) == 3:
        my_tree.set_outgroup(my_tree.get_leaves()[0])
    assert set([len(i.children) for i in my_tree.traverse() if not i.is_leaf()]) == set([2])
    ###Identifying the two leaves that are farthest from one-another
    starting, trash = my_tree.get_farthest_leaf()
    farthest1, init_dist = starting.get_farthest_node()
    farthest2, max_dist = farthest1.get_farthest_node()
    assert farthest1.is_leaf() and farthest2.is_leaf()
    
    ###Actually performing the mid-point root
    final_root(my_tree, farthest1, farthest2, max_dist)
    
    ###Making sure the two leave are equi-distant from one-another
    assert np.isclose(my_tree.get_distance(farthest1), my_tree.get_distance(farthest2))
    ###Making sure that I didn't lose any branch length along the way
    final_bl = np.sum([i.dist for i in my_tree.traverse()])
    assert np.isclose(init_bl, final_bl)
    ###Making sure I didn't lose any leaves along the way
    assert set(init_term_names) == set([i.name for i in my_tree.get_leaves()])
    ###And that I'm still fully bifurcating
    assert set([len(i.children) for i in my_tree.traverse() if not i.is_leaf()]) == set([2])
    return

def get_ancestor_path(parent, target):
    temp_node = target
    path = []
    while temp_node != parent:
        path.append(temp_node)
        temp_node = temp_node.up
    return path

def get_shortest_path(my_tree, node1, node2):
    lca = my_tree.get_common_ancestor(node1, node2)
    path1 = get_ancestor_path(lca, node1)
    path2 = get_ancestor_path(lca, node2)
    path2 = path2[::-1] ###Reverse this list to correctly orient the final path
    path = path1+path2
    return path

def final_root(my_tree, farthest1, farthest2, max_dist):
    """
    """
    path = get_shortest_path(my_tree, farthest1, farthest2)
    assert np.isclose(np.sum([i.dist for i in path]), max_dist)
    ###Finding the correct branch for the final root
    mid_point = max_dist/2.
    counter = 0
    for node in path:
        counter += node.dist
        if counter < mid_point:
            last_success = node
        else:
            remainder = counter - mid_point
            break        
    ###Rooting the my_tree accordingly
    my_tree.set_outgroup(node)
    ###Checking the orientation (asking whether the other node is indeed a child)
    if my_tree.children[0] != node:
        my_tree.swap_children()
    ###If the topology doesn't get deformed by the rooting
    if my_tree.children == [node, last_success]:
        total = np.sum([i.dist for i in my_tree.children])
        my_tree.children[0].dist = remainder
        my_tree.children[1].dist = total-remainder
    ###And if it does induce a topology deformation
    else:
        assert last_success in my_tree.children[1].children        
        total = np.sum([i.dist for i in my_tree.children + [last_success]])
        my_tree.children[0].dist = remainder
        my_tree.children[1].dist = 0.
        last_success.dist = total-remainder
    return