class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        back_j = -1
        match_i = 0
        m = len(s)
        n = len(p)
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < n and p[j] == "*":
                back_j = j
                match_i = i
                j += 1
            elif back_j != -1:
                j = back_j + 1
                match_i += 1
                i = match_i
            else:
                return False
            print(p[j:])
        return list(p[j:]).count("*") == len(p[j:])
