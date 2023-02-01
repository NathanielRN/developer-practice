# https://leetcode.com/problems/all-elements-in-two-binary-search-trees

# Definition for a binary tree node.

from typing import List
from Python.helper import *

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = self.f(root1) + self.f(root2)
        result.sort()
        return result

    def f(self, root):
        s = []
        result = []
        curr = root
        while s or curr:
            if curr:
                s.append(curr)
                curr = curr.left
            else:
                curr = s.pop()
                result.append(curr.val)
                curr = curr.right

        return result


sln = Solution().getAllElements(
    get_tree_from_array([2, 1, 4]), get_tree_from_array([1, 0, 3])
)
print(sln)
