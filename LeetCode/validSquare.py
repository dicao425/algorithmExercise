#!/usr/bin/python
import sys


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        d = dict()
        p = (p1, p2, p3, p4)
        for i in range(4):
            for j in range(i + 1, 4):
                v = self.get_dist(p[i], p[j])
                d[v] = d.get(v, 0) + 1
        return len(d.values()) == 2 and 0 not in d

    def get_dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())