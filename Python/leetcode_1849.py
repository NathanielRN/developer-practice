# Backtracking question.

class Solution:
    def splitString(self, s: str) -> bool:
        if len(s) == 1:
            return False

        def findValid(index, prev_num) -> bool:
            if index == len(s):
                return True
            
            for jump in range(index + 1, len(s) + 1):
                chars = s[index: jump]
                num = int(chars)
                if num == prev_num - 1:
                    if findValid(jump, num):
                        return True

            return False

        return any(findValid(start, int(s[:start])) for start in range(1, len(s)))


"""
Trying a recurse backwards approach...
class Solution
    def splitString(self, s: str) -> bool:
        if len(s) == 1:
            return False

        def recurseCheckDescending(start: int) -> Tuple[bool, Optional[int]]:
            if start == len(s):
                return True, None
            
            for jump in range(start + 1, len(s) + 1):
                curr_chars = s[start:jump]
                curr_num = int(curr_chars)

                is_valid, next_num = recurseCheckDescending(jump)

                if is_valid or next_num + 1 == curr_num:
                    return curr_num
                
            return None

        last_integer = recurseCheckDescending(0)

        return last_integer is not None
"""

"""
# ChatGPT:
class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index: int, prev: int, count: int) -> bool:
            # Base case: processed the entire string
            if index < 0:
                return count >= 2  # need at least two numbers

            num = 0
            factor = 1
            for i in range(index, -1, -1):
                digit = int(s[i])
                num = digit * factor + num
                factor *= 10

                if s[i] == '0' and i != index:
                    continue  # skip numbers with leading zeros

                if prev == -1 or num + 1 == prev:
                    if dfs(i - 1, num, count + 1):
                        return True

            return False

        return dfs(len(s) - 1, -1, 0)

"""