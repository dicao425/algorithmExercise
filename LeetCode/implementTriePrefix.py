#!/usr/bin/python
import sys


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        def _search(node, i):
            if i == len(word):
                return node.isEnd
            if word[i] in node.children:
                return _search(node.children[word[i]], i + 1)
            else:
                return False

        return _search(self.root, 0)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        def _search(node, i):
            if i == len(prefix):
                return True
            if prefix[i] in node.children:
                return _search(node.children[prefix[i]], i + 1)
            else:
                return False

        return _search(self.root, 0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def main():
    aa = Trie()
    aa.insert("a")
    print aa.search("a")
    print aa.startsWith("a")
    return 0

if __name__ == "__main__":
    sys.exit(main())
