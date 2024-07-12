
# get the IR expression of the block as a string list
def IRS(block):
    IRList = block.vex.statements
    IRListStr = []
    for IRStatement in IRList:
        IRListStr.append(IRStatement.IRStmt.pp_str())
    return IRListStr
