from features.node_name import HandleNodeName

def FindMatching1(refPath, longestPath):
    matchingList = []
    for node1 in refPath:
        for node2 in longestPath:
            if (HandleNodeName(node1.name) == HandleNodeName(node2.name)):
                if ((len(node1.successors) == len(node2.successors)) & (len(node1.predecessors) == len(node2.predecessors))):
                    matchingList.append([node1, node2])
                    longestPath.remove(node2)
                    break
    return matchingList

def FindMatching2(refPath, longestPath):
    matchingList = []
    for node1 in refPath:
        for node2 in longestPath:
            if ((len(node1.successors) == len(node2.successors)) & (len(node1.predecessors) == len(node2.predecessors))):
                matchingList.append([node1, node2])
                longestPath.remove(node2)
                break
    return matchingList
    