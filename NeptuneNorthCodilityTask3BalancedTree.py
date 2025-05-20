class Node:
    children = []
    def __init__(self, children):
        self.children = children

def Solution(tree) -> int:
    if len(tree.children) == 0: # leaf condition
        return 1
    elif len(tree.children) > 0: # subtree condition
        # if a node has children, then calculate all childrens' subtree sizes
        childSizes = []
        for node in tree.children:
            childSizes.append(Solution(node))

        balanceCheck = len(set(childSizes))
        if balanceCheck > 1: # not balanced
            return sum(childSizes)
        elif balanceCheck == 1: # balanced, each child tree is same size, so add 1
            return sum(childSizes) + 1

    return 0

a = Node([])
b = Node([])
c = Node([a,b])
d = Node([])
e = Node([d])
f = Node([c,e])

s = Solution(b)
print(s)
print(Solution(f))