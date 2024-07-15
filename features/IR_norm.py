
def IRNorm(insn):

    for i in range(0, len(insn)):
        IRs = insn[i]
        if ('PUT' in IRs):
            insn[i] = 'PUT'
        elif ('STle' in IRs):
            insn[i] = 'Store'
        elif ('LDle' in IRs):
            insn[i] = 'Load'
        elif ('WrTmp' in IRs):
            insn[i] = 'Write'
        elif ('RdTmp' in IRs):
            insn[i] = 'Read'
        elif ('GET' in IRs):
            insn[i] = 'GET'
        elif ('ITE' in IRs):
            insn[i] = 'ITE'
        elif ('Add' in IRs):
            insn[i] = 'Add'
        elif ('Sub' in IRs):
            insn[i] = 'Sub'
        elif (IRs[0:2] == 'if'):
            insn[i] = 'if'
        else:
            start = 0
            end = 0
            for j in range(0, len(IRs)):
                if (IRs[j] == '='):
                    start = j
                if (IRs[j] == '('):
                    end = j
            if (start < end):
                insn[i] = IRs[start+1:end]
            elif (start > 0):
                insn[i] = '='
    
    return list(insn)