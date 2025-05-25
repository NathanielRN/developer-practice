""""
LRU Cache
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in 
O(1)
O(1) average time complexity.

Example 1:

Input:
["LRUCache [2], "put [1, 10],  "get [1], "put [2, 20], "put [3, 30], "get [2], "get [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)
Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000
"""

from typing import Dict

class DoubleNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return (
            "Node("
            f"key={self.key}, "
            f"val={self.val}, "
            f"prev={self.prev.val if self.prev else None}, "
            f"next={self.next.val if self.next else None})"
        )

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: Dict[int, DoubleNode] = {}
        self.head = DoubleNode("HEAD", "DUMMY")
        self.tail = DoubleNode("TAIL", "DUMMY")
        self.tail.prev = self.head
        self.head.next = self.tail

    def print_linked_list(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.addToFront(node)
        
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.addToFront(node)

            node.val = value
        else:
            node = DoubleNode(key, value)
            self.addToFront(node)
            self.cache[key] = node
            if len(self.cache) == self.capacity + 1:
                # We ignore the tail node because it is a dummy node.
                del self.cache[self.tail.prev.key]
                # We want to keep the tail dummy node so that we can continue to
                # ignore it next time. Also, we can trust that the head dummy
                # node exists so that we can go backwards prev 2 times.
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def addToFront(self, node) -> None:
        if node.prev: 
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # This code is explicitly ignoring the first node. That's okay, because
        # it is a dummy node.
        node.next = self.head.next
        self.head.next.prev = node
        # Since we are ignoring dummy nodes, we need to keep the dummy node so
        # that we can continue to ignore it in the future!
        node.prev = self.head
        self.head.next = node

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
expected = lru.get(1)
assert expected == 1

lru.put(3, 3)
expected = lru.get(2)
assert expected == -1

lru.put(4, 4)
expected = lru.get(1)
assert expected == -1

expected = lru.get(3)
assert expected == 3

expected = lru.get(4)
assert expected == 4
