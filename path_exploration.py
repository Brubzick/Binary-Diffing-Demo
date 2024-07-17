from compare1 import BlockCompare
from queue import Queue
import compare2

# path exploration / get cfg score table
# Define Score and GNode to store the previous node in the path
# so that the path can be traceback
class Score:
    score = 0
    gnode = None
    pre = None
    def __init__(self, node, pre, score):
        self.gnode = node
        self.pre = pre
        self.score = score

class GNode:
    node = None
    pre = node
    index = 0
    def __init__(self, node, pre, index):
        self.node = node
        self.pre = pre
        self.index = index

def IfInPath(gNodeS, gNode):
    # avoid loop
    while (gNode):
        if (gNode.node == gNodeS.node):
            return True
        gNode = gNode.pre    
    return False

def PathExplore(cfg, path):
    pLength = len(path)
    # The score table stores Score
    #first columns and first rows are 0s to convenient the calculation
    gTable = [[Score(None,None,0)]*(pLength+1)] 
    row_num = 0
    nodeList = list(cfg.nodes())
    hScore = [0]*len(nodeList) 
    head = GNode(nodeList[0], None, 0)
    q = Queue()
    q.put(head)

    while (not q.empty()):
        row_num += 1
        gNode = q.get()
        gNode.index = row_num
        cNode = gNode.node
        # add a row
        gTable.append([Score(None,None,0)]*(pLength+1))

        for col_num in range(1, pLength+1):
            simScore = 0
            if ((len(cNode.predecessors) == len(path[col_num-1].predecessors)) & (len(cNode.successors) == len(path[col_num-1].successors))):
                simScore = compare2.BlockCompare(cNode, path[col_num-1])

            score = max(gTable[row_num-1][col_num].score, gTable[row_num][col_num-1].score, gTable[row_num-1][col_num-1].score+simScore)
            gTable[row_num][col_num] = Score(gNode, gNode.pre, score)

        cNodeIndex = nodeList.index(cNode)
        if ((hScore[cNodeIndex] < score) | (hScore[cNodeIndex] == 0)):
            hScore[cNodeIndex] = score
            for i in range(0, len(cNode.successors)):
                gNode_t = GNode(cNode.successors[i],gNode, 0)
                if (not IfInPath(gNode_t, gNode)):
                    q.put(gNode_t)
    
    return gTable