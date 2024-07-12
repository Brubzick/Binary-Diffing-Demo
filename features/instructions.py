# get instructions (capstone_insn), entry node at head
def GetIns(cfg):
    
    insList = []

    for node in cfg.nodes():
        if (not node.is_simprocedure):
            for insn in node.block.insns:
                insList.append(insn)

    return insList
