from path_exploration import PathExplore
from compare1 import BlockCompare
from neighborhood_explore import NeighborEx, IfConflict
from features.find_longest_path import FindLongest
from features.reference_path import getRefPath
import compare2
from features.node_name import HandleNodeName
from find_matching_node import FindMatching1

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
    matchingList = FindMatching1(refPath,path)

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

