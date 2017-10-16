#!/usr/bin/python
import sys

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for p in points:
            d = {}
            for q in points:
                a = p[0] - q[0]
                b = p[1] - q[1]
                d[a*a + b*b] = d.get(a*a + b*b, 0) + 1
            for k in d:
                result += d[k] * (d[k]-1)
        return result

def main():
    aa = Solution()
    print aa.numberOfBoomerangs()
    return 0

if __name__ == "__main__":
    sys.exit(main())
