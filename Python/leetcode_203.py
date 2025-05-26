# Similar question but not the exact same question.


# 4 -> 3 -> 2 -> 1 -> 1 -> 1

from typing import Optional, Tuple

class Node:
    val: int
    next: Optional[Node]

    def __init__(self, val: int):
        self.val = val
        self.next = None

def removeKthNodeFromEnd(k: int, head: Node) -> Optional[Node]:
    dummy_node = Node(None)
    dummy_node.next = head
    head = dummy_node

    _, sub_problem_found_target_node = _recurseRemoveKthNodeFromEnd(k, head)

    return sub_problem_found_target_node

def _recurseRemoveKthNodeFromEnd(k: int, head: Node) -> Tuple[int, Optional[Node]]:
    if head.next is None:
        return 1, None
    
    sub_problems_depth, node = _recurseRemoveKthNodeFromEnd(k, head.next)

    if sub_problems_depth is None:
        return None, node
    
    my_depth = sub_problems_depth + 1

    if my_depth == k + 1:
        target: Node = head.next
        head.next = head.next.next
        target.next = None
        return None, target

    return my_depth, None
