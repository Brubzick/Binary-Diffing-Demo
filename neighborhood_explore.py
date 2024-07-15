from compare1 import BlockCompare
import numpy as np
from scipy.optimize import linear_sum_assignment
from queue import PriorityQueue
import compare2

def IfSameSuc(node1, node2):
    if(len(node1.successors) == len(node2.successors)):
        return True
    return False

def IfSamePre(node1, node2):
    if(len(node1.predecessors) == len(node2.predecessors)):
        return True
    return False

# map neighbors
def NeighborMapping(neighborhood1, neighborhood2):
    l = len(neighborhood1)
    if (l == 1):
        return [[neighborhood1[0], neighborhood2[0]]]
    else:
        # Hungarian Algorithm
        H = [[0]*l]*l
        for i in range(0,l):
            for j in range(0,l):
                score = compare2.BlockCompare(neighborhood1[i], neighborhood2[j])
                if (score == 0):
                    H[i][j] = 1000
                else:
                    H[i][j] = 1/score
        sim = np.asarray(H)
        comb = linear_sum_assignment(sim)

        # output the result
        mapping = []
        for i in range(0,l):
            mapping.append([neighborhood1[comb[0][i]], neighborhood2[comb[1][i]]])
        
        return mapping

# only explore 1 layer 只探索了相邻的节点，没有继续深入 
def NeighborEx(matchinglist):
    new_mapping = []
    q = PriorityQueue()
    index = 0 # secondary priority number
    for pair in matchinglist:
        score = compare2.BlockCompare(pair[0],pair[1])
        if (score != 0):
            q.put((1/score,index,pair))
        index += 1
    # start neighbor explore
    while (not q.empty()):
        pair = q.get()[2]
        node1 = pair[0]
        node2 = pair[1]
        if (IfSameSuc(node1, node2) & ((len(node1.successors) != 0))):
            mapping = NeighborMapping(node1.successors, node2.successors)
            new_mapping.extend(mapping)
    
        if (IfSamePre(node1,node2) & (len(node1.predecessors) != 0)):
            mapping = NeighborMapping(node1.predecessors, node2.predecessors)
            new_mapping.extend(mapping)

    return new_mapping

# used to check if the new mapping conflict the old matching
def IfConflict(map1, maplist):
    for map2 in maplist:
        if ((map1[0] == map2[0]) | (map1[1] == map2[1])):
            return True
    return False