class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if stack:
                top = stack[-1]
                if (top == "A" and i == "B") or (top == "C" and i == "D"):
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)


# Example 1
# s = "ABTTTTTABTTTTTAB"

# Example 2
# s = "AACDBB"


# Example 3
# s = "ACDABB"

# Example 4
# s = "BABABA"

# Leetcode 1
# s = "ABFCACDB"
