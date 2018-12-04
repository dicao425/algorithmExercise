#!/usr/bin/python
import sys

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = dict()
        for i, w in enumerate(words):
            self.words[w] = self.words.get(w, []) + [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = float('inf')
        w1 = self.words.get(word1)
        w2 = self.words.get(word2)
        i1 = 0
        i2 = 0
        while i1 < len(w1) and i2 < len(w2):
            if w1[i1] < w2[i2]:
                result = min(result, w2[i2] - w1[i1])
                i1 += 1
            else:
                result = min(result, w1[i1] - w2[i2])
                i2 += 1
        return result


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())