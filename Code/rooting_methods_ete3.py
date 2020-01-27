import numpy as np

def MP_root_ete3(tree):
    """
    
    """
    init_bl = np.sum([i.dist for i in tree.traverse()])
    init_terms = tree.get_leaves()
    init_term_names = [i.name for i in tree.get_leaves()]
    if len(tree.children) == 3:
        tree.set_outgroup(tree.get_leaves()[0])
    assert set([len(i.children) for i in tree.traverse() if not i.is_leaf()]) == set([2])
    ###Identifying the two leaves that are farthest from one-another
    starting, trash = tree.get_farthest_leaf()
    farthest1, init_dist = starting.get_farthest_node()
    farthest2, max_dist = farthest1.get_farthest_node()
    assert farthest1.is_leaf() and farthest2.is_leaf()
    
    ###Actually performing the mid-point root
    final_root(tree, farthest1, farthest2, max_dist)
    
    ###Making sure the two leave are equi-distant from one-another
    assert np.isclose(tree.get_distance(farthest1), tree.get_distance(farthest2))
    ###Making sure that I didn't lose any branch length along the way
    final_bl = np.sum([i.dist for i in tree.traverse()])
    assert np.isclose(init_bl, final_bl)
    ###Making sure I didn't lose any leaves along the way
    assert set(init_term_names) == set([i.name for i in tree.get_leaves()])
    ###And that I'm still fully bifurcating
    assert set([len(i.children) for i in tree.traverse() if not i.is_leaf()]) == set([2])
    return

def final_root(tree, farthest1, farthest2, max_dist):
    """
    This is brutal and needs to be simplified even though it works fine
    """
    ###An annoyingly convoluted way to get the path between two nodes, ignoring the dist of the LCA
    lca = tree.get_common_ancestor(farthest1, farthest2)
    temp_node = farthest1
    path1 = []
    while temp_node != lca:
        path1.append(temp_node)
        temp_node = temp_node.up
    temp_node = farthest2
    path2 = []
    while temp_node != lca:
        path2.append(temp_node)
        temp_node = temp_node.up
    path2 = path2[::-1]
    path = path1+path2
    
    ###Finding the correct branch for the final root
    counter = 0
    for i,j in zip([i.dist for i in path], path):
        counter += i
        if counter < max_dist/2:
            old_path = j
            continue
        else:
            remainder = counter - (max_dist/2)
            counter -= i
            break
            
    ###Rooting the tree accordingly
    if len(path) > 0:
        tree.set_outgroup(old_path)
        if tree.children == [old_path, j]:
            total = np.sum([i.dist for i in tree.children])
            tree.children[1].dist = remainder
            tree.children[0].dist = total-remainder
        else:
            tree.set_outgroup(j)
            total = np.sum([i.dist for i in tree.children])
            tree.children[0].dist = remainder
            tree.children[1].dist = total-remainder
    else:
        tree.set_outgroup(farthest2)
    return

