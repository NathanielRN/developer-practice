class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        levelStart = root

        while levelStart is not None:
            curr = levelStart
            while curr is not None:
                if curr.left:
                    curr.left.next = curr.right
                if curr.right and curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next
            levelStart = levelStart.left

        return root
