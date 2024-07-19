from compare1 import BlockCompare
import numpy as np
from scipy.optimize import linear_sum_assignment
from queue import PriorityQueue
import compare2

def IfSameSuc(node1, node2):
    if((len(node1.successors) == len(node2.successors)) & (len(node1.successors) != 0)):
        return True
    return False

def IfSamePre(node1, node2):
    if((len(node1.predecessors) == len(node2.predecessors)) & (len(node1.predecessors) != 0)):
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
                H[i][j] = -score
        sim = np.asarray(H)
        comb = linear_sum_assignment(sim)

        # output the result
        mapping = []
        for i in range(0,l):
            mapping.append([neighborhood1[comb[0][i]], neighborhood2[comb[1][i]]])
        
        return mapping
 
def NeighborEx(matchinglist):
    new_mapping = []
    q = PriorityQueue()
    qSuc = PriorityQueue()
    qPre =  PriorityQueue()
    index = 0 # secondary priority number
    deep_level = 5 # set explore level to avoid dead loop
    layer = 0
    for pair in matchinglist:
        score = compare2.BlockCompare(pair[0],pair[1])
        q.put((-score,index,pair))
        index += 1
    # start neighbor explore
    while (not q.empty()):
        pair = q.get()[2]
        node1 = pair[0]
        node2 = pair[1]
        if (IfSameSuc(node1, node2)):
            mapping = NeighborMapping(node1.successors, node2.successors)
            new_mapping.extend(mapping)

            for nodePair in mapping:
                if (IfSameSuc(nodePair[0], nodePair[1])):
                    score = compare2.BlockCompare(nodePair[0],nodePair[1])
                    qSuc.put((-score, index, nodePair))
                    index += 1
    
        if (IfSamePre(node1,node2)):
            mapping = NeighborMapping(node1.predecessors, node2.predecessors)
            new_mapping.extend(mapping)

            for nodePair in mapping:
                if (IfSamePre(nodePair[0], nodePair[1])):
                    score = compare2.BlockCompare(nodePair[0],nodePair[1])
                    qPre.put((-score, index, nodePair))
                    index += 1
    layer = 0
    while (not qSuc.empty()):
        layer += 1
        if layer >= deep_level:
            break
        pair = qSuc.get()[2]
        node1 = pair[0]
        node2 = pair[1]
        if (IfSameSuc(node1, node2)):
            mapping = NeighborMapping(node1.successors, node2.successors)
            new_mapping.extend(mapping)

            for nodePair in mapping:
                if (IfSameSuc(nodePair[0], nodePair[1])):
                    score = compare2.BlockCompare(nodePair[0],nodePair[1])
                    qSuc.put((-score, index, nodePair))
                    index += 1
    layer = 0
    while (not qPre.empty()):
        layer += 1
        if layer >= deep_level:
            break
        pair = qPre.get()[2]
        node1 = pair[0]
        node2 = pair[1]

        if (IfSamePre(node1,node2)):
            mapping = NeighborMapping(node1.predecessors, node2.predecessors)
            new_mapping.extend(mapping)

            for nodePair in mapping:
                if (IfSamePre(nodePair[0], nodePair[1])):
                    score = compare2.BlockCompare(nodePair[0],nodePair[1])
                    qPre.put((-score, index, nodePair))
                    index += 1

    return new_mapping

# used to check if the new mapping conflict the old matching
def IfConflict(map1, maplist):
    for map2 in maplist:
        if ((map1[0] == map2[0]) | (map1[1] == map2[1])):
            return True
    return False