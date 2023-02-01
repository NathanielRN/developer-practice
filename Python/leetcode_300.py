from typing import List, Dict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [ 1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
        # 

        # [ 1, -1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = len(nums)

        def LIS(current_offset: int, next_offset: int, memo: Dict[int, int]):
            if next_offset == n:
                return 0

            if current_offset in memo:
                return memo[current_offset]

            with_current = 0
            if current_offset == -1 or nums[next_offset] > nums[current_offset]:
                with_current = 1 + LIS(next_offset, next_offset + 1, memo)
            
            without_current = LIS(current_offset, next_offset + 1, memo)
            
            memo[current_offset] = max(with_current, without_current)
            return memo[current_offset]
        
        return LIS(-1, 0, {})

answer = Solution().lengthOfLIS([1, -1, 2, 3, 4, 5, 6, 7, 8, 9])

print(answer)