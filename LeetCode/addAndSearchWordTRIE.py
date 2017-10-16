#!/usr/bin/python
import sys

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isEnd = True

    def search(self, word):
        def _search(node, w, i):
            if i == len(word):
                return node.isEnd
            if word[i] == '.':
                for ch, n in node.children.items():
                    if _search(n, w+ch, i+1):
                        return True
            else:
                if word[i] in node.children:
                    if _search(node.children[word[i]], w+word[i], i+1):
                        return True
            return False
        return _search(self.root, '', 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
'''
["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
'''
def main():
    aa = WordDictionary()
    aa.addWord("at")
    aa.addWord("and")
    aa.addWord("an")
    aa.addWord("add")
    print aa.search("a")
    print aa.search(".at")
    aa.addWord("bat")
    print aa.search(".at")
    print aa.search("an.")
    print aa.search("a.d.")
    print aa.search("b.")
    print aa.search("a.d")
    print aa.search(".")
    return 0

if __name__ == "__main__":
    sys.exit(main())
