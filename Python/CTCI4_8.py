class Result:
    def __init__(self, root, is_ancestor):
        self.root = root
        self.is_ancestor = is_ancestor


def findCommonAncestor(root, p, q):
    result = commonAncestorHelper(root, p, q)

    if result.is_ancestor:
        return result.root

    return None

def commonAncestorHelper(root, p, q):
    if not root:
        return Result(None, True)
    
    if root == p and root == q:
        return Result(root, True)
    
    rx = commonAncestorHelper(root.left, p, q)

    if rx.is_ancestor:
        return rx
    
    ry = commonAncestorHelper(root.right, p, q)

    if ry.is_ancestor:
        return ry
    
    if rx.root and ry.root:
        return Result(root, True)
    elif root == p or root == q:
        return Result(root, rx.root or ry.root)
    else:
        return Result(rx.root if rx.root else ry.root, False)