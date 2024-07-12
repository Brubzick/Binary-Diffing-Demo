from features.ins_normalization import InsNorm

# compare instruction
def InsCompare(ins1, ins2):
    ins1 = InsNorm(ins1)
    ins2 = InsNorm(ins2)
    category = ['reg', 'memRef', 'memOffset']
    score = 0
    l = min(len(ins1), len(ins2))
    if ins1[0] == ins2[0]: # same mnemonic
        score += 2
    for i in range(1, l):
        if (ins1[i] == ins2[i]):
            if (ins1[i] in category):
                score += 1 # same type oprand
            else:
                score += 3 # same constant
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
            


