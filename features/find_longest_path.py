# Find the longest path in a CFG
# dpsNode that can store its last node in the current path
class dpsNode:
    node = None
    pre = None
    cStep = 0
    def __init__(self, node, pre, cStep):
        self.node = node
        self.pre = pre
        self.cStep = cStep

def InPath(node, pathNode):
    while (pathNode):
        if (node.node == pathNode.node):
            return True
        pathNode = pathNode.pre
    return False

def FindLongest(cfg):
    head = list(cfg.nodes())[0]
    stack = [] #work stack
    lNode = None # the leaf dpsNode of the longest path
    cPathLeaf = None # the leaf of current path
    maxStep = 0
    stack.append(dpsNode(head, None, 0))

    while (stack):
        cNode = stack.pop()
        if (InPath(cNode, cPathLeaf)):
            continue
        else:
            tNode = cNode.node
            cPathLeaf = cNode
            if (tNode.successors):
                for node in tNode.successors:
                    stack.append(dpsNode(node, cNode, cNode.cStep+1))
            else:
                if (cNode.cStep > maxStep):
                    maxStep = cNode.cStep
                    lNode = cNode

    # get longest path
    lPath = []
    while (lNode):
        lPath.append(lNode.node)
        lNode = lNode.pre
    lPath.reverse()

    return lPath

    



