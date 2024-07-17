from features.IR_expression import IRExpression
from features.node_name import HandleNodeName

# compare instruction
def InsnCompare(insn1, insn2):

    l1 = len(insn1)
    l2 = len(insn2)
    scoreTable = [[0]*l2]*l1

    for i in range(1, l1):
        for j in range(1, l2):
            if (insn1[i] == insn2[j]):
                score = 1
            else:
                score = 0
            scoreTable[i][j] = max(scoreTable[i-1][j], scoreTable[i][j-1], scoreTable[i-1][j-1]+score)

    return scoreTable[l1-1][l2-1]

# compare block
def BlockCompare(node1, node2):
    if (node1.is_simprocedure | node2.is_simprocedure):
        if (HandleNodeName(node1.name) == HandleNodeName(node2.name)):
            return 1
        else:
            return 0
    else:
        insns1 = IRExpression(node1.block)
        insns2 = IRExpression(node2.block)
        l1 = len(insns1)
        l2 = len(insns2)
        bTable = [[0]*(l2+1)]*(l1+1) #first columns and first rows are 0s to convenient the calculation

        for i in range(1, l1+1):
            for j in range(1,l2+1):
                bTable[i][j] = max(bTable[i-1][j],bTable[i][j-1],bTable[i-1][j-1]+InsnCompare(insns1[i-1], insns2[j-1]))

        return bTable[l1][l2]