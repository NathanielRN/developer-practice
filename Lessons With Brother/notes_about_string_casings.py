from typing import List

def getAllCasingsOfString(target: str) -> List[str]:
    getAllCasingsOfString(target, 0)

def getAllCasingsOfString(target: str, start: int) -> List[str]:
    if len(target) == 1:
        return [target.upper(), target.lower()]
    
    results = []

    for i in range(start, len(target)):
        current_letter = target[i]
        answer_without_i = getAllCasingsOfString(target[0:i] + target[i+1:], i)
        
        results.extend([answer.insertAt(i) for answer in answer_without_i])

    return results

def getAllCombinationsOfString(target: str) -> List[str]:
    if len(target) == 1:
        return [target]
    
    for i in range(len(target)):
        answer = getAllCombinationsOfString(target[0:i], target[i+1:])







class Node:
    right: Node
    left: Node

    def __init__(self, right=None, left=None):
        self.right = right
        self.left = left


a = Node()
a.right = Node()
a.left = Node()

b = Node()
b.right = a

#              B
#           /    \
#        C        A
#       / \      / \
#     T    U    W   X
#
# [T, U, W, X]

visited = set()

def dfs(root, target) -> Node:
    visited.add(root)
    if root == target:
        return root
    if root.left not in visited:
        dfs(root.left, target)
    if root.right not in visited:
        dfs(root.right, target)

def bfs(root, target) -> Node:
    queue = []
    queue.append(root)

    while queue:
        current = queue[0]
        if current == target:
            return current
        queue.append(current.left)
        queue.append(current.right)
        queue.remove(current)

    return None














