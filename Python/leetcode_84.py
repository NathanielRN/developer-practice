# https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/

class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

sln = Solution().largestRectangleArea([1, 2, 3, 4, 5])

print(sln)

# 94 / 94 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# 97.34%