# Find the longest path in a CFG
# use deep first search method, avoid loop

# dfsNode that can store its previous node in the current path
class dfsNode:
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
    lNode = None # the leaf dfsNode of the longest path
    cPathLeaf = None # the leaf of current path
    maxStep = 0
    stack.append(dfsNode(head, None, 0))
    count = 0

    while (stack):
        cNode = stack.pop()
        if (InPath(cNode, cPathLeaf)):
            continue
        else:
            tNode = cNode.node
            cPathLeaf = cNode
            if (tNode.successors):
                for node in tNode.successors:
                    stack.append(dfsNode(node, cNode, cNode.cStep+1))
            else:
                count += 1
                if (cNode.cStep > maxStep):
                    maxStep = cNode.cStep
                    lNode = cNode
                if (count >= 1000000):
                    print('too many pathes, use the current longest path.')
                    break

    # get longest path
    lPath = []
    while (lNode):
        lPath.append(lNode.node)
        lNode = lNode.pre
    lPath.reverse()
    return lPath

def TracebackLongest(node, head):
    stack = []
    hNode = None
    cPathHead = None
    maxStep = 0
    count = 0
    stack.append(dfsNode(node, None, 0))

    while(stack):
        cNode = stack.pop()
        if (InPath(cNode, cPathHead)):
            continue
        else:
            tNode = cNode.node
            cPathHead = cNode
            if ((tNode == head) |(tNode.predecessors == [])):
                count += 1
                if (cNode.cStep > maxStep):
                    maxStep = cNode.cStep
                    hNode = cNode
                if (count >= 1000000):
                    print('too many pathes, use the current longest path.')
                    break
            else:
                for node in tNode.predecessors:
                    stack.append(dfsNode(node, cNode, cNode.cStep+1))       

    # get longest path
    lPath = []
    while (hNode):
        lPath.append(hNode.node)
        hNode = hNode.pre
    return lPath


