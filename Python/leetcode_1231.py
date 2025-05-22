from typing import List

class Solution:
    def maximizeSweetness(sweetness: List[int], K: int):
        def canDivide(minSweet):
            count = 0
            curr = 0
            for s in sweetness:
                curr += s
                if curr >= minSweet:
                    count += 1
                    curr = 0
            return count >= K + 1

        low, high = 1, sum(sweetness) // (K + 1)
        while low < high:
            mid = (low + high + 1) // 2
            if canDivide(mid):
                low = mid
            else:
                high = mid - 1
        return low