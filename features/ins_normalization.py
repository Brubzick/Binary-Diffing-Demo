
reg = ['eax','ebx','ecx','edx','esi','edi','ebp', 'esp',
       'r8d','r9d','r10d','r11d','r12d','r13d','r14d','r15d',
       'al','bl','cl','dl','sil','dil','bpl','spl',
       'r8b','r9b','r10b','r11b','r12b','r13b','r14b','r15b',
       'ax','bx','cx','dx','si','di','bp','sp',
       'r8w','r9w','r10w','r11w','r12w','r13w','r14w','r15w',
       'rax','rbx','rcx','rdx','rsi','rdi','rbp','rsp',
       'r8','r9','r10','r11','r12','r13','r14','r15']

# normalize instruction
# instructions are normalized onto a string list containing mnemonic and oprands
# oprands are classified into
# ['reg', 'memRef', 'memOffset', 'Constant'(keep the number)]
def InsNorm(insn):
    mnemonic = insn.mnemonic
    oprand = insn.op_str.split()
    l = len(oprand)
    start = 0
    end = 0

    if l >= 2:
        # remove ','
        for i in range(0, l):
            if (oprand[i][-1] == ','): 
                oprand[i] = oprand[i][:-1]
        # combine '[ ]'
        for i in range(0, l):
            if (oprand[i][0] == '['):
                start = i
            if (oprand[i][-1] == ']'):
                end = i
        if ((start != 0) & (end != 0)):
            oprand[start] = 'memRef'
            for i in range(start, end):
                oprand.remove(oprand[start+1])
                l = len(oprand) #update the length   
        # memory offset and constant
        for i in range(0, l):
            if (oprand[i][-1] == 'h'):
                if ((len(oprand[i]) == 8) | (len(oprand[i]) == 16)):
                    oprand[i] = 'memOffset'
        #  handle 'ptr'
        for i in range(1, l):
            if (oprand[i] == 'ptr'):
                oprand[i-1] = 'memRef'
                oprand.remove(oprand[i])
                oprand.remove(oprand[i])
                l = len(oprand) #update the length 
                break
        # register
        for i in range(0, l):
            if (oprand[i] in reg):
                oprand[i] = 'reg'
    
    normList = [mnemonic]
    normList.extend(oprand)
    return normList