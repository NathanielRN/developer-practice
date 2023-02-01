class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sor = ''.join(sorted(s))
            if sor in d:
                d[sor].append(s)
            else:
                d[sor] = [s]
        ans = list(d.values())
        return ans