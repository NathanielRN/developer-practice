from typing import List

# Example:
# a/bb/a/tt/uu

# Recurse forward solution

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        pali_cache = {}  # Cache for palindrome checks
        dfs_cache = {}   # Cache for dfs results starting at index i

        def isPali(i, j):
            if (i, j) in pali_cache:
                return pali_cache[(i, j)]

            if i >= j:
                pali_cache[(i, j)] = True
                return True

            if s[i] != s[j]:
                pali_cache[(i, j)] = False
                return False

            pali_cache[(i, j)] = isPali(i + 1, j - 1)
            return pali_cache[(i, j)]

        def dfs(i):
            # E.g.
            # Prefix: abba
            # SourceToDrain: ttuu
            # AllResults: [..., [abba, tt, u, u], [abba, tt, uu], ...]

            if i in dfs_cache:
                # Replay cached subtrees
                for cached_path in dfs_cache[i]:
                    res.append(part + cached_path)
                return

            if i >= len(s):
                res.append(part.copy())
                return

            original_res_len = len(res)
            for j in range(i, len(s)):
                if isPali(i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

            # Cache new results added during this dfs call
            # After removing the prefix `abba`: [..., [tt, u, u], [tt, uu], ...]
            dfs_cache[i] = [r[len(part):] for r in res[original_res_len:]]

        dfs(0)
        return res


# Recurse backwards solution

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i, cache) -> List[List[str]]:
            if i == len(s):
                return []

            if i in cache:
                return cache[i]

            all_results = [] # [[t, t, u, u], [t, t, uu], [tt, u, u], [tt, uu], [ttuu]]

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    palindrome = s[i : j + 1] # tt
                    if j + 1== len(s):
                        all_results.append(palindrome)
                        continue

                    sub_problem_solutions = dfs(j + 1) # [[u,u], [uu]]
                    merged_solutions = []

                    for sub_soln in sub_problem_solutions:
                        merged_soln = [palindrome] + sub_soln
                        merged_solutions.append(merged_soln)

                    all_results.extend(merged_solutions) #[[tt, u, u], [tt, uu]]

            cache[i] = all_results

            return all_results

        res = dfs(0, {})
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True