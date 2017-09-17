#!/usr/bin/python
import sys

class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = {}

class Solution(object):
    def insertWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.root = TrieNode()
        for w in words:
            self.insertWord(w)
        self.board = board
        self.result = []
        for j in range(len(board)):
            for i in range(len(board[0])):
                self.dfs(i, j, '', self.root)
        return self.result

    def dfs(self, i, j, word, trie):
        if trie.word:
            self.result.append(word)
            trie.word = False
            # Maybe the word like (boy  boyfriend), continue searching
        if i<0 or j<0 or i>=len(self.board[0]) or j>=len(self.board):
            return
        if self.board[j][i] in trie.children:
            tmp_ch, self.board[j][i] = self.board[j][i], '#'
            self.dfs(i+1, j, word+tmp_ch, trie.children[tmp_ch])
            self.dfs(i, j+1, word+tmp_ch, trie.children[tmp_ch])
            self.dfs(i, j-1, word+tmp_ch, trie.children[tmp_ch])
            self.dfs(i-1, j, word+tmp_ch, trie.children[tmp_ch])
            self.board[j][i] = tmp_ch
        return


def main():
    mm = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    word = ["oath","pea","eat","rain"]
    aa = Solution()
    print aa.findWords(mm, word)
    return 0

if __name__ == "__main__":
    sys.exit(main())