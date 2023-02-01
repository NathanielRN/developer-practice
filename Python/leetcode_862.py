from typing import List
from collections import deque

# This is the prefix queue question you are probably thinking about...

def shortestSubarray(self, nums: List[int], k: int) -> int:
    current_sum = 0
    shortest = float("inf")
    prefix_queue = deque([(0, current_sum)])

    for i in range(len(nums)):
        current_sum += nums[i]
        while prefix_queue and current_sum - prefix_queue[0][1] >= k:
            shortest = min(shortest, i - prefix_queue.popleft()[0] + 1)
        while prefix_queue and current_sum <= prefix_queue[-1][1]:
            prefix_queue.pop()
        prefix_queue.append((i + 1, current_sum))

    return shortest if shortest != float("inf") else -1


shortestSubarray([89, 67, 99, 25, 29], 166)

