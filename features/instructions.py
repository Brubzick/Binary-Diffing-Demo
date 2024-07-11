# get instructions as a string list, entry node at head
def GetIns(cfg):
    
    nodeList = list(cfg.nodes())

    insList = []

    for node in nodeList:
        if (not node.is_simprocedure):
            l = node.block.instructions
            for i in range(0, l):
                insList.append(str(node.block.capstone.insns[i]))

    return insList
