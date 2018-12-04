#!/usr/bin/python
import sys

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        for i in range(len(words1)):
            if words1[i] == words2[i] or [words1[i], words2[i]] in pairs or [words2[i], words1[i]] in pairs:
                continue
            else:
                return False
        return True

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())