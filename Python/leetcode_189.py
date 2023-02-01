from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # [ 1, 2, 3, 4, 4, -5 ], k = 3
        # [ 4, 4, -5, 1, 2, 3 ]
        # Solution: Runtime=O(n), Memory=O(k)
        # Other Solution: Runtime=O(n), Memory=O(n)
        # Other Solution: Runtime = O(kn), Memory=O(1)

        # Easy test cases:
        if k == 0 or k == len(nums):
            return
        
        

        # Remember last k elements
        k_last_elements = nums[-k:]

        # Jump

        # Sort
        
        # Iterate through all elements

        #
