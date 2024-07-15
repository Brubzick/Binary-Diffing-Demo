from features.IR_norm import IRNorm
from features.IR_expression import IRS

# compare instruction
def InsnCompare(ins1, ins2):
    insn1 = IRNorm(ins1)
    insn2 = IRNorm(ins2)

    l1 = len(insn1)
    score = 0

    for i in range(0, l1):
        for word in insn2:
            if (insn1[i] == word):
                score += 1
                insn2.remove(word)
                break

    final_score = score/l1
    return(final_score)

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
        insnList1 = IRS(node1.block)
        insnList2 = IRS(node2.block)
        l1 = len(insnList1)
        l2 = len(insnList2)
        bTable = [[0]*(l2+1)]*(l1+1) #first columns and first rows are 0s to convenient the calculation

        for i in range(1, l1+1):
            for j in range(1,l2+1):
                bTable[i][j] = max(bTable[i-1][j],bTable[i][j-1],bTable[i-1][j-1]+InsnCompare(insnList1[i-1], insnList2[j-1]))

        return bTable[l1][l2]