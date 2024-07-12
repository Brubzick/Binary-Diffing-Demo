import angr
import pyvex
from features.find_longest_path import FindLongest
from features.ins_normalization import InsNorm
from main_compare import Compare

proj = angr.Project('./angr_ctf/dist/09_angr_hooks', auto_load_libs = False)

cfg = proj.analyses.CFGFast(normalize=True)
cg = cfg.kb.callgraph

edge1 = list(cg.edges)[0]
a,b,c = edge1

print(cfg.get_any_node(a))
print(cfg.get_any_node(b))