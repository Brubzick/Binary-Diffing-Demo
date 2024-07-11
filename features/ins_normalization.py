
reg = ['eax','ebx','ecx','edx','esi','edi','ebp', 'esp',
       'r8d','r9d','r10d','r11d','r12d','r13d','r14d','r15d',
       'al','bl','cl','dl','sil','dil','bpl','spl',
       'r8b','r9b','r10b','r11b','r12b','r13b','r14b','r15b',
       'ax','bx','cx','dx','si','di','bp','sp',
       'r8w','r9w','r10w','r11w','r12w','r13w','r14w','r15w',
       'rax','rbx','rcx','rdx','rsi','rdi','rbp','rsp',
       'r8','r9','r10','r11','r12','r13','r14','r15']

# normalize instruction
# oprands are classified into
# ['reg', 'memRef', 'memOffset', 'Constant'(keep the number)]
def InsNorm(ins):
    sList = str(ins).split()
    sList.remove(sList[0])
    l = len(sList)
    start = 0
    end = 0

    if l >= 2:
        # remove ','
        for i in range(1, l):
            if (sList[i][-1] == ','): 
                sList[i] = sList[i][:-1]
        # combine '[ ]'
        for i in range(1, l):
            if (sList[i][0] == '['):
                start = i
            if (sList[i][-1] == ']'):
                end = i
        if ((start != 0) & (end != 0)):
            sList[start] = 'memRef'
            for i in range(start, end):
                sList.remove(sList[start+1])
                l = len(sList) #update the length   
        # memory offset and constant
        for i in range(1, l):
            if (sList[i][-1] == 'h'):
                if ((len(sList[i]) == 8) | (len(sList[i]) == 16)):
                    sList[i] = 'memOffset'
                else:
                    sList[i] = sList[i][:-1]
        #  handle 'ptr'
        for i in range(1, l):
            if (sList[i] == 'ptr'):
                sList[i-1] = 'memRef'
                sList.remove(sList[i])
                sList.remove(sList[i])
                l = len(sList) #update the length 
                break
        # register
        for i in range(1, l):
            if (sList[i] in reg):
                sList[i] = 'reg'
    return sList