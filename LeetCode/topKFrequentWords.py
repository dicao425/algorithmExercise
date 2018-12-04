#!/usr/bin/python
import sys

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = dict()
        for w in words:
            d[w] = d.get(w, 0) + 1
        return [i[0] for i in sorted(d.items(), key=lambda x: (-x[1], x))[
                              :k]]  # lambda x: (-x[1], x) first sort by number, second sort by word in alphb

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())