from typing import List


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        def combinationSum(selected: List[int], offset: int) -> List[List[int]]:
            results = []

            for i in range(offset, len(candidates)):
                n_selected = selected + [candidates[i]]
                new_sum = sum(n_selected)

                if new_sum == target:
                    results.append(n_selected)
                elif new_sum < target:
                    results.extend(combinationSum(n_selected, i))

            return results

        return combinationSum([], 0)


sln = Solution().combinationSum([2, 7, 6, 3, 5, 1], 9)
print(sln)
