#!/usr/bin/python
import sys

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = None
        i2 = None
        result = float('inf')
        for idx, w in enumerate(words):
            if w == word1:
                i1 = idx
            if w == word2:
                i2 = idx
            if i1 is not None and i2 is not None:
                result = min(result, abs(i1-i2))
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())