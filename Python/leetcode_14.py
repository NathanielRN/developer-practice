# 1. Read the question well, and write down a summary
# 2. Identify data structure you want to use
# 3. Write commented code
# 4. Think of edge cases.
# 5. Write the code (Keep asking your interviewer, if they understand. Communicate!!!)
# 6. Read through the code
# 7. Run through a test case

# Inputs:
# * strings: List[String]

# Outputs:
# * longestCommonPrefix: String

# NOTES:
# * It is a COMMON prefix
# * If there is no common prefix, return an empty string "".

# Constaints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List

# ['apple', 'banana', 'orange'] -> ''
# ['apple', 'app', 'index', 'apple', 'applepie'] -> ''

def findLongestCommonPrefix(strs: List[str]) -> str:
    # Immediately set longest prefix to 1st element. If the length is 1, just exit early. Constraint 1.
    if len(strs) == 1:
        return strs[0]

    # Store in just 1 variable `longestCommonPrefix`, because the question said all strings must have it in common.
    longestCommonPrefix = strs[0]

    # Iterate through the strings, but start at the 2nd, if there is one.
    for newString in strs[1:]:
        # If no characters, I can quit the whole function because there is nothing in common.
        
        # if newString == '' or newString == None or len(newString) == 0:
        # Also, if the longest string is an empty, there's no point in looking anymore, they are all different.
        if not newString or not longestCommonPrefix:
            return ''

        smallerString = newString if len(newString) < len(longestCommonPrefix) else longestCommonPrefix

        changedLongestCommonPrefix = False
        # Iterate through the characters in the current string. Compare it to the current longest prefix. Compare by the smaller one.
        for index in range(0, len(smallerString)):
            newStringChar = newString[index]
            longestCommonPrefixChar = longestCommonPrefix[index]

            # If it is smaller, then you have to replace. It will not be bigger, because the prefix can only get smaller.
            if newStringChar != longestCommonPrefixChar:
                changedLongestCommonPrefix = True
                longestCommonPrefix = newString[:index]
                break

        if not changedLongestCommonPrefix:
            longestCommonPrefix = smallerString
    
    # Return the store 1 variable `longestCommonPrefix`.
    return longestCommonPrefix