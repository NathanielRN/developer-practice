# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/submissions/

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # for every group, check if g is in nums
        start = 0
        for g in groups:
            found = False
            for i in range(start, len(nums) - len(g) + 1):
                if nums[i : i + len(g)] == g:
                    found = True
                    start = i + len(g)
                    break
            if not found:
                return False
        return True
