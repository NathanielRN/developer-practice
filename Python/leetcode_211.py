# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self, isTerminal=False):
        self.children = {}
        self.isTerminal = isTerminal

    def addAndGetChild(self, child_string):
        if child_string not in self.children:
            self.children[child_string] = TrieNode()

        return self.children[child_string]

    def getChild(self, child_string):
        return self.children[child_string]

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for word_char in word:
            curr = curr.addAndGetChild(word_char)
        
        curr.isTerminal = True

    def search(self, word: str) -> bool:
        def searchFromI(start: int, curr: TrieNode) -> bool:

            for i in range(start, len(word)):
                word_char = word[i]
                if word_char == '.':
                    return any([
                        searchFromI(i + 1, next_curr)
                        for next_curr in curr.children.values()
                    ])
                elif word_char in curr.children:
                    curr = curr.children[word_char]
                else:
                    return False

            return curr.isTerminal
        
        return searchFromI(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)