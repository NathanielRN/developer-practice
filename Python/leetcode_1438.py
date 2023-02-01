from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque([0])
        min_deque = deque([0])
        longest = 1
        start = -1
        
        for i in range(1, len(nums)):
            while len(max_deque) > 0 and nums[i] >= nums[max_deque[-1]]:
                max_deque.pop()
            
            while len(min_deque) > 0 and nums[i] <= nums[min_deque[-1]]:
                min_deque.pop()
            
            max_deque.append(i)
            min_deque.append(i)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] < min_deque[0]:
                    start = max_deque.popleft()
                else:
                    start = min_deque.popleft()
            
            longest = max(longest, i - start)
        
        return longest
        