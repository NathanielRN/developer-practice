from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0

        queue = deque()

        queue.append((root, 0, 0))

        level_left = 0
        level_right = 0

        previous_level = -1

        while queue:
            node, level, pos = queue.popleft()

            if previous_level != level:
                local_max_width = level_right - level_left + 1
                max_width = max(max_width, local_max_width)
                level_left = float("inf")
                level_right = -float("inf")
                previous_level = level

            if node.left:
                child_pos = 2 * pos
                queue.append((node.left, level, child_pos))
                level_left = min(level_left, child_pos)
                level_right = max(level_right, child_pos)

            if node.right:
                child_pos = 2 * pos + 1
                queue.append((node.right, level, child_pos))
                level_right = max(level_right, child_pos)
                level_left = min(level_left, child_pos)

        local_max_width = level_right - level_left + 1
        max_width = max(max_width, local_max_width)

        return max_width


answer = Solution().cherryPickup(
    [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        None,
        None,
        None,
        1,
        None,
        None,
        None,
        None,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        None,
        2,
        None,
        None,
        2,
        None,
        2,
    ]
)

print(answer)
