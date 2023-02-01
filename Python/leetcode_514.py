import copy


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # ring = godding
        # key = gd
        # Output = 4

        # ggdiggd
        # key = di
        # Output = 5

        # g: 0, 1, 2, 3
        # d: 1, 2
        # i: 3

        # ggdigde
        # key = ide
        # Output = 6
        queue = [(0, 0)]

        cost = 0

        n = len(ring)

        while True:
            newQueue = []
            for curr_index, seen_length in queue:
                if ring[curr_index] == key[seen_length]:
                    if seen_length + 1 == len(key):
                        return cost + len(key) + 1

                    cost -= 1
                    newQueue.append((curr_index, seen_length + 1))
                    break

                # Go right
                right = (curr_index + 1) % n
                newQueue.append((right, seen_length))

                # Go left
                left = (curr_index - 1) % n
                newQueue.append((left, seen_length))
            queue = newQueue
            cost += 1
        return -1


answer = Solution().findRotateSteps("edcba", "abcde")

print(answer)
