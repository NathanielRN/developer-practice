

# Examples
# 'AAB'
# [A], [AA], []



class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        pass



class Solution:
    # find ways to do:
    # - scambled dont use everything (susbsets)
    # - scrambled use everything (permutations)
    # - ordered dont use everything (susbsets)
    # - ordered used everything with index (memo)
    # index is good when you want to use everything (index = str)
    
    # 11
    # 1 - 1
    # total = 2

    def numDecodingsOrderedUsingEverything(self, s: str) -> int:
        memo = {}

        def numWays(index: int) -> int:
            if index == len(s):
                return 1

            if index in memo:
                return memo[index]

            total = 0

            one_char = int(s[index: index + 1])

            if one_char > 0 and one_char < 10:
                total += numWays(index + 1)

            if index <= len(s) - 2:

                two_char = int(s[index: index + 2])
                if two_char < 27 and two_char > 9:
                    total += numWays(index + 2)

            memo[index] = total

            return memo[index]

        return numWays(0)

    def numCodingsOrderedNotEverthing(self, s: str) -> int:

        def findGroupings(index: int) -> int:
            if index == len(s):
                return 0
            if index in memo:
                return memo[index]

            total = 0

            
            one_char = int(s[index:index + 1])

            if one_char > 0 and one_char < 10:
                total += 1
                total += findGroupings(index + 1)

            if index <= len(s) - 2:

                two_char = int(s[index: index + 2])

                if two_char > 9 and two_char < 27:
                    total += 1
                    total += findGroupings(index + 2)

            memo[index] = total

            return memo[index]

        return findGroupings(0)


    def numCodingsScrambledDontUseEverything(self, s: str) -> int:
        def findGroupings(remainingChars: str) -> int:
            if len(remainingChars) == 1:
                return 1

            if len(remainingChars) == 2:
                return 4

            total = 0

            # ab -> ab, ba, a, b

            # aaa da/efaaa

            # remove duplicates
            seen_prefix_characters = set()

            for i, char in enumerate(remainingChars):
                if char in seen_prefix_characters:
                    continue

                seen_prefix_characters.add(char)

                sub_str = s[i] + s[i+1:]
                
                total += findGroupings(sub_str) * 2

                for j, char2 in sub_str:
                    prefix = char + char2
                    if prefix in set():
                        continue

                    seen_prefix_characters.add(prefix)

                    sub_sub_str = sub_str[j] + sub_str[j+1:]

                    total += findGroupings(sub_sub_str) * 2

            return total

        return findGroupings(0, s)
    # https://leetcode.com/problems/restore-ip-addresses/description/
