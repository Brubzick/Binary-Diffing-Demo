# get reference path from similarity table in compare 1 method
def getRefPath(simTable):
    l1 = len(simTable)-1
    l2 = len(simTable[0])-1
    highest = simTable[l1][l2]
    for i in range(l1,0,-1):
        for j in range(l2,0,-1):
            if (simTable[i][j].score > highest.score):
                highest = simTable[i][j]
            
    refPath = []
    nodeTrace = highest.gnode
    while (nodeTrace):
        refPath.append(nodeTrace.node)
        nodeTrace = nodeTrace.pre
    
    refPath.reverse() # reference path
    return refPath