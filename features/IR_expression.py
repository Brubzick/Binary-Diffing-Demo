
def IRExpression(block):
    IRStatements = block.vex.statements
    insns = []
    insn = []

    for IRStmt in IRStatements:
        tag = IRStmt.tag
        if ((tag == 'Ist_IMark')):
            if (insn != []):
                insns.append(insn)
            insn = []
        insn.append(tag)
    if (insn != []):
        insns.append(insn)
    
    return insns
