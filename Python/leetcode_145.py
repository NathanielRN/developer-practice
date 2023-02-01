# https://leetcode.com/problems/binary-tree-postorder-traversal/



class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]

# 2 3 1
# 1 2 3
# 1 3 2