from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        array = list(map(str, nums))

        # Custom sorting with a lambda function
        # The maximum number that the input can be is 10**9, so if you multiply
        # each string by 10 you guarantee matching the digits of the string to
        # the highest possible candidate
        # (e.g. 9 vs 90 becomes 9999999999 vs 909090...9090 which makes 9 the larger number)
        array.sort(key=lambda x: x * 10, reverse=True)

        # Handle the case where the largest number is "0"
        if array[0] == "0":
            return "0"

        # Build the largest number from the sorted array
        largest = "".join(array)

        return largest


ans = Solution().largestNumber([34323, 3432])
assert ans == "343234323", f"Got ans={ans}"

ans = Solution().largestNumber([34, 3, 37])
assert ans == "37343", f"Got ans={ans}"

ans = Solution().largestNumber([9, 53, 5, 59, 8])
assert ans == "9859553", f"Got ans={ans}"
