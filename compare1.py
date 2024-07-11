from queue import Queue
from features.ins_normalization import InsNorm

# compare instruction
def InsCompare(ins1, ins2):
    ins1 = InsNorm(ins1)
    ins2 = InsNorm(ins2)
    category = ['reg', 'memRef', 'memOffset']
    score = 0
    l = min(len(ins1), len(ins2))
    if ins1[0] == ins2[0]:
        score += 2
    for i in range(1, l):
        if (ins1[i] == ins2[i]):
            if (ins1[i] in category):
                score += 1
            else:
                score += 3
    return score

# compare block
def BlockCompare(node1, node2):
    if (node1.is_simprocedure & node2.is_simprocedure):
        # blocks that contain no instructions
        if (node1.name == node2.name):
            return 1
        else:
            return 0
    elif (node1.is_simprocedure | node2.is_simprocedure):
        return 0
    else:
        l1 = node1.block.instructions
        l2 = node2.block.instructions
        bTable = [[0]*(l2+1)]*(l1+1) #first columns and first rows are 0s to convenient the calculation

        for i in range(1, l1+1):
            for j in range(1,l2+1):
                bTable[i][j] = max(bTable[i-1][j],bTable[i][j-1],bTable[i-1][j-1]+InsCompare(node1.block.capstone.insns[i-1], node2.block.capstone.insns[j-1]))

        return bTable[l1][l2]

# path exploration / get cfg score table
# Define Score and GNode to store the previous node in the path
# so that the path can be traceback
# class Score:
#     score = 0
#     gnode = None
#     pre = None
#     def __init__(self, node, pre, score):
#         self.gnode = node
#         self.pre = pre
#         self.score = score

# class GNode:
#     node = None
#     pre = node
#     index = 0
#     def __init__(self, node, pre, index):
#         self.node = node
#         self.pre = pre
#         self.index = index

# def PathExplore(cfg, path):
#     pLength = len(path)
#     # The score table stores Score
#     #first columns and first rows are 0s to convenient the calculation
#     gTable = [[Score(None,None,0)]*(pLength+1)] 
#     row_num = 0
#     nodeList = list(cfg.nodes())
#     hScore = [0]*len(nodeList) 
#     head = GNode(nodeList[0], None, 0)
#     q = Queue()
#     q.put(head)

#     while (not q.empty()):
#         row_num += 1
#         gNode = q.get()
#         gNode.index = row_num
#         cNode = gNode.node
#         # add a row
#         gTable.append([Score(None,None,0)]*(pLength+1))

#         for col_num in range(1, pLength+1):
#             simScore = 0
#             if (
#             (len(cNode.predecessors) == len(path[col_num-1].predecessors)) & 
#             (len(cNode.successors) == len(path[col_num-1].successors))
#             ):
#                 simScore = BlockCompare(cNode, path[col_num-1])
#             score = max(gTable[row_num-1][col_num].score, gTable[row_num][col_num-1].score, gTable[row_num-1][col_num-1].score+simScore)
#             gTable[row_num][col_num] = Score(gNode, gNode.pre, score)

#         cNodeIndex = nodeList.index(cNode)
#         if (hScore[cNodeIndex] < score):
#             hScore[cNodeIndex] = score
#             for i in range(0, len(cNode.successors)):
#                 q.put(GNode(cNode.successors[i],gNode, 0))
    
#     return gTable
            


