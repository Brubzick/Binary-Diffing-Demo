import angr
from features.find_longest_path import FindLongest
from features.ins_normalization import InsNorm
from main_compare import Compare
from features.IRExpression import IRS

proj = angr.Project('./angr_ctf/dist/00_angr_find', auto_load_libs = False)

cfg = proj.analyses.CFGFast(normalize=True)

count = 0


# for node in cfg.nodes():
#     count += 1
#     if (not node.is_simprocedure):
#         for ins in IRS(node.block):
#             print(ins)
#     if count >= 3:
#         break