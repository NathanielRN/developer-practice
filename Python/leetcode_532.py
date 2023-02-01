class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        ctr = Counter(nums)
        res = 0

        for x in ctr:
            if k > 0 and x + k in ctr:
                res += 1
            if k == 0 and ctr[x] > 1:
                res += 1

        return res
