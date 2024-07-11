import random

def RandomPath(node):
    randPatn = []
    while (node.successors != []):
        randPatn.append(node)
        i = random.randrange(0, len(node.successors))
        node = node.successors[i]
    return randPatn
