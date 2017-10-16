#!/usr/bin/python
import sys
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # BFS
        q = [(beginWord, 1)]
        #if endWord not in wordList:
        #    wordList.append(endWord)
        s = set(wordList)
        while q:
            curr_word, curr_step = q.pop(0)
            if curr_word == endWord:
                return curr_step
            for p in range(len(beginWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == curr_word[p]:
                        continue
                    new_word = curr_word[:p] + c + curr_word[p+1:]
                    if new_word in s:
                        q.append((new_word, curr_step+1))
                        s.remove(new_word)
        return 0
def main():
    aa = Solution()
    print aa.ladderLength()
    return 0

if __name__ == "__main__":
    sys.exit(main())
