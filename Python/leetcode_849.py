from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prevIndex = -1
        res = 0
        for i, val in enumerate(seats):
            if val:
                if prevIndex == -1:
                    prevIndex = i
                    if not seats[0]:
                        res = max(res, prevIndex)
                else:
                    res = max(res, (i - prevIndex) // 2)
                    prevIndex = i
        if not seats[-1]:
            res = max(res, (len(seats) - 1 - prevIndex))
        return res
