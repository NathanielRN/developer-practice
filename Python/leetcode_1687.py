from typing import List


class Solution:
    def boxDelivering(
        self,
        boxes: List[List[int]],
        portsCount: int,
        maxBoxes: int,
        maxWeight: int,
    ) -> int:
        n = len(boxes)
        dp = [0] * n
        left = -1
        ans = 0
        for right in range(n):
            maxBoxes -= 1
            maxWeight -= boxes[right][1]
            if left + 1 == right:
                ans += 2
            elif boxes[right][0] != boxes[right - 1][0]:
                ans += 1
            while (
                maxBoxes < 0
                or maxWeight < 0
                or (left + 1 != right and dp[left] == dp[left + 1])
            ):
                left += 1
                maxBoxes += 1
                maxWeight += boxes[left][1]
                if boxes[left][0] != boxes[left + 1][0]:
                    ans -= 1
            dp[right] = dp[left] + ans
        return dp[-1]


sln = Solution()
ans = sln.boxDelivering([[1, 1], [2, 1], [1, 1]], 2, 3, 3)
print(ans)
