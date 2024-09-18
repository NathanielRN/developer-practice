from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def uncommonWordsInASentence(s):
            mySet = set()
            commonMySet = set()
            for w in s.split(" "):
                if w in mySet:
                    commonMySet.add(w)
                else:
                    mySet.add(w)

            mySet -= commonMySet

            return mySet

        setA = uncommonWordsInASentence(s1)
        setB = uncommonWordsInASentence(s2)

        uncommon = [a for a in setA if a not in s2.split(" ")] + [
            b for b in setB if b not in s1.split(" ")
        ]

        return uncommon
