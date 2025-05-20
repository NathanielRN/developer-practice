"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""

from typing import List


# Example 1:
# - Input: [-1, -2, 6,7,8,1,2,3,4,5]
# - Answer: 8

# Example 2:
# - Input: [1,2,3,4,5]
# - Answer: 5

# Example 3:
# - Input: [6,7,8,1,2,3,4,5]
# - Answer: 8

# Restrictions
# - In O(n) time.

class Solution:
    def longestConsecutiveSequence(nums: List[int]) -> int:
        pass
        # [5, 8, 7, 2, 6, 3, 1, 4, -5]
        #
        # [5, 8,]

        
        # use a set ->removes duplicates allows O(1) search
        # create variable for current max
        # Create vairable for overall max
        # iterate through set and ask a question

            # if current contains a left number in the set
                # skip
            # else 
                # iterate from this number until the end
                    # Increment current max counter
                    # Break once next number not in set
                # Get max of current max and overall max
 
        # return overall max



        