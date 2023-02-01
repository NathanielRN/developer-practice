# https://leetcode.com/problems/jump-game-vii/submissions/

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Check for Easy Cases
        # there are several places having the last index was convenient, so I compute/store it here
        I = len(s) - 1

        if s[I] == "1":
            # It's Impossible to Land on the Target
            return False
        elif minJump == maxJump:
            # There's Only 1 Possible Path
            return I % minJump == 0 and all(
                c == "0" for c in s[minJump:I:minJump]
            )
        elif minJump == 1:
            # Check if There's an Un-Jumpable String of 1's
            return "1" * maxJump not in s
        else:
            # Solve the Puzzle Using the Method of Your Choice
            # Compute the Bounds for Finishing
            visited = set()
            return self.dfs(s, 0, minJump, maxJump, visited)

    def dfs(self, s, i, minJ, maxJ, v):
        if i == len(s) - 1:
            return True

        left = i + minJ
        right = min(i + maxJ, len(s) - 1)

        v.add(i)
        for j in range(right, left - 1, -1):
            if s[j] == "0" and j not in v:
                if self.dfs(s, j, minJ, maxJ, v):
                    return True
        return False
