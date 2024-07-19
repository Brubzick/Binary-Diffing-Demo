from path_exploration import PathExplore
from neighborhood_explore import NeighborEx, IfConflict
from features.find_longest_path import FindLongest, TracebackLongest
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


def Compare2(proj1, proj2):
    cfg1 = proj1.analyses.CFGFast(normalize=True) # reference
    cfg2 = proj2.analyses.CFGFast(normalize=True) # target
    head1 = cfg1.get_any_node(proj1.entry)
    head2 = cfg2.get_any_node(proj2.entry)

    leafNodes1 = []
    leafNodes2 = []
    for node in cfg1.nodes():
        if node.successors == []:
            leafNodes1.append(node)

    for node in cfg2.nodes():
        if node.successors == []:
            leafNodes2.append(node)
    matchingPairs = []
    for node1 in leafNodes1:
        pair = []
        for node2 in leafNodes2:
            if (HandleNodeName(node1.name) == HandleNodeName(node2.name)):
                if (len(node1.predecessors) == len(node2.predecessors)):
                    pair = [node1, node2]
                    break
        if (pair != []):
            matchingPairs.append(pair)

    finalScore = 0
    for pair in matchingPairs:
        path1 = TracebackLongest(pair[0], head1)
        path2 = TracebackLongest(pair[1], head2)

        matchingList = FindMatching1(path1, path2)
        
        # neighborhood explore
        new_mapping = NeighborEx(matchingList)
        for map1 in new_mapping:
            # check if conflict
            if (not IfConflict(map1, matchingList)):
                matchingList.append(map1)

        for i in range(0, len(matchingList)):
            finalScore += compare2.BlockCompare(matchingList[i][0], matchingList[i][1])
    
    return finalScore
