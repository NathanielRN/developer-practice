class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_tree_from_array(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])

    queue = [root]

    i = 1
    while i < len(arr):
        node = queue.pop(0)

        left = TreeNode(arr[i])
        node.left = left
        queue.append(left)

        if i + 1 < len(arr):
            right = TreeNode(arr[i + 1])
            node.right = right
            queue.append(right)

        i += 2

    return root