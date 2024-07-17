import angr
from features.find_longest_path import FindLongest
from features.ins_normalization import InsNorm
from main_compare import Compare
from features.IR_expression import IRS

proj = angr.Project('./bfs')

block = proj.factory.block(proj.entry)

ins = block.vex.statements[0]

print([] == None)