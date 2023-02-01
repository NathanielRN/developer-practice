from typing import List
import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_p = 0
        next_p = 0
        step = 0
        for i in range(len(nums) - 1):
            next_p = max(next_p, i + nums[i])
            if cur_p == i:
                step += 1
                cur_p = next_p
        return step

sln = Solution()
ans = sln.jump([2, 3, 1, 1, 4])
print(ans)