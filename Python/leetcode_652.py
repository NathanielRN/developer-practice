# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = {}
        
        ans = []
        
        def dfs_post(node):
            if not node:
                # Important to distinguish left vs right node is NULL
                return "X"
            
            components = [str(node.val)]
            
            left_serialized = dfs_post(node.left)
            
            if left_serialized:
                components.append(left_serialized)
            
            right_serialized = dfs_post(node.right)
            
            if right_serialized:
                components.append(right_serialized)
            
            node_serialized = ",".join(components)
            
            if node_serialized not in seen:
                seen[node_serialized] = False
            elif seen[node_serialized] == False:
                ans.append(node)
                seen[node_serialized] = True
            
            return node_serialized
        
        dfs_post(root)
        
        return ans