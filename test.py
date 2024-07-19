import angr
from compare2 import BlockCompare
from main_compare import Compare
from features.IR_expression import IRExpression
from features.find_longest_path import TracebackLongest
from features.node_name import HandleNodeName

proj1 = angr.Project("./dfs", auto_load_libs = False)
proj2 = angr.Project("./dfs3", auto_load_libs = False)

cfg1 = proj1.analyses.CFGFast(normalize=True)
cfg2 = proj2.analyses.CFGFast(normalize=True)

leafNodes1 = []
leafNodes2 = []

for node in cfg1.nodes():
    if node.successors == []:
        leafNodes1.append(node)

for node in cfg2.nodes():
    if node.successors == []:
        leafNodes2.append(node)

matchingPairs = []

for node1 in leafNodes1:
    pair = []
    for node2 in leafNodes2:
        if (HandleNodeName(node1.name) == HandleNodeName(node2.name)):
            if (len(node1.predecessors) == len(node2.predecessors)):
                pair = [node1, node2]
                break
    if (pair != []):
        matchingPairs.append(pair)

print(matchingPairs)