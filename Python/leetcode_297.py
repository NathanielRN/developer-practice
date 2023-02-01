
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#       1
#   2           3
#           4           5
#                      6

# [1, 2, 3, X, X, 4, 5, X, X, 6, X]

#               1
#      2                    3
#    X    X             4        5
#                     X.  X.   6    X

class Codec:
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        queue = []
        
        queue.append(root)
        
        ans = [str(root.val)]
        
        while queue:
            node = queue.pop(0)
            
            if node.left:
                ans.append(str(node.left.val))
                queue.append(node.left)
            else:
                ans.append("X")
            
            if node.right:
                ans.append(str(node.right.val))
                queue.append(node.right)
            else:
                ans.append("X")
        
        return ",".join(ans)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # data: [1, 2, 3, X, X, 4, 5, X, X, 6, X]
        if not data:
            return None
        
        data_elements = data.split(",")
        
        root = TreeNode(data_elements[0])
        
        #                  1
        #       2                   3
        #                      4        5
        #                       
        
        # queue: [ 6N ]
        queue = [root]
        
        i = 1
        
        # i: 7
        while i < len(data_elements):
            # left: 6
            left = data_elements[i]
            
            if left != "X":
                left_node = TreeNode(int(left))
                queue[0].left = left_node
                queue.append(left_node)
            
            if i + 1 < len(data_elements):
                # right: X
                right = data_elements[i + 1]
                
                if right != "X":
                    right_node = TreeNode(int(right))
                    queue[0].right = right_node
                    queue.append(right_node)        
            
            queue.pop(0)
            i += 2
        
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))