
def IRS(block):
    IRList = block.vex.statements
    IRInsnList = []
    insn = []
    
    for IRStatement in IRList:
        statement = IRStatement.pp_str()
        if (statement[0] == '-'):
            if (insn != []):
                IRInsnList.append(insn)
            insn = []
        else:
            insn.append(statement)
    if (insn != []):
        IRInsnList.append(insn)

    return IRInsnList