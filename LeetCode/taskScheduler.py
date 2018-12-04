#!/usr/bin/python
import sys

import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        v = collections.Counter(tasks).values()
        M = max(v)
        Mct = v.count(M)
        return max(len(tasks), (M-1) * (n+1) + Mct)
    # A A A B B C C C    n = 2
    # A C B A C B A C _
    # M = 3 - 1 (A) blocks  ex: [A__A__]A
    # Every block has n+1 items "A__" 2+1 (A)
    # Rest is the max items A and C appended

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())