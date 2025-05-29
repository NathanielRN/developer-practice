"""
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.
"""


# plan/understanding
# str = '11' -> aa or k -> 2
# Example = '112' -> aab or kb or aj
# How human
# 1 -> a, 1 - > a, 2 - > b
# 1 -> a 12 -> j
# 11 -> k 2 -> b

# Data structure/algorithms
# dictionary for codes
# recursion
# backtracking

# Base case - > if we have 2 numbers then return
# recursive step -> adding numbers to my str

# Test Case
# '112'
#
# index = 0
# total = 3
# curr_s = '27'
# budget = '1': 2, '2': 1

# Input: '1'

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         memo = {}

#         def numWays(index: int) -> int:
#             if index == len(s):
#                 return 1

#             if index in memo:
#                 return memo[index]

#             total = 0

#             one_char = int(s[index: index + 1])

#             if one_char > 0 and one_char < 10:
#                 total += numWays(index + 1)

#             if index <= len(s) - 2:

#                 two_char = int(s[index: index + 2])
#                 if two_char < 27 and two_char > 9:
#                     total += numWays(index + 2)

#             memo[index] = total

#             return memo[index]

#         return numWays(0)


#    '1  3'
# [1, 1, 2]
# 1234238974/5
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        N = len(s)

        dp = [0] * (N + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, N + 1):
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]

            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[N]