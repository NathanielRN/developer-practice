class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.helper(s)

    def helper(self, s):
        if s == "":
            return 1
        if len(s) == 1 and s == "0":
            return 0
        if len(s) == 1:
            return 1
        # if len(s) == 2 and s[0] != '0' and int(s) <= 26: return 1
        if s in self.memo:
            return self.memo[s]

        first = self.helper(s[1:]) if s[0] != "0" else 0
        second = self.helper(s[2:]) if s[0] != "0" and int(s[:2]) <= 26 else 0
        res = first + second
        self.memo[s] = res
        return res


sln = Solution().numDecodings("12")
print(sln)
