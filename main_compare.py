from path_exploration import PathExplore
from compare1 import BlockCompare
from neighborhood_explore import NeighborEx, IfConflict
from features.find_longest_path import FindLongest
from features.reference_path import getRefPath
from features.node_name import HandleNodeName
import compare2

def Compare(proj1, proj2):
    cfg1 = proj1.analyses.CFGFast(normalize=True) # reference
    cfg2 = proj2.analyses.CFGFast(normalize=True) # target
    
    # longest path
    path = FindLongest(cfg2)

    # score table
    simTable = PathExplore(cfg1, path)

    # reference path
    refPath = getRefPath(simTable)    

    # find matching node
    matchingList = []
    for node1 in refPath:
        for node2 in path:
            if (HandleNodeName(node1.name) == HandleNodeName(node2.name)):
                if ((len(node1.successors) == len(node2.successors)) & (len(node1.predecessors) == len(node2.predecessors))):
                    matchingList.append([node1, node2])
                    path.remove(node2)
                    break

    # neighborhood explore
    new_mapping = NeighborEx(matchingList)
    for map1 in new_mapping:
        # check if conflict
        if (not IfConflict(map1, matchingList)):
            matchingList.append(map1)

    finalScore = 0
    for i in range(0, len(matchingList)):
        finalScore += compare2.BlockCompare(matchingList[i][0], matchingList[i][1])

    return finalScore


def Compare2(proj1, proj2):
    cfg1 = proj1.analyses.CFGFast(normalize=True) # reference
    cfg2 = proj2.analyses.CFGFast(normalize=True) # target
    
    # longest path
    path = FindLongest(cfg2)

    # score table
    simTable = PathExplore(cfg1, path)

    # reference path
    refPath = getRefPath(simTable)

    # LCS
    row = len(refPath)+1
    col = len(path)+1
    table = [[0]*col]*row

    for i in range(1, row):
        for j in range(1, col):
            table[i][j] = max(table[i-1][j], table[i][j-1], table[i-1][j-1]+compare2.BlockCompare(refPath[i-1], path[j-1]))
    
    return table[row-1][col-1]
