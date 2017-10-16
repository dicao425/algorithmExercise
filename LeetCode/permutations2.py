#!/usr/bin/python
import sys

class Solution(object):
    def permuteUnique(self, nums):
        result = [[]]
        for n in nums:
            g = []
            for l in result:
                for i in xrange(len(l)+1):
                    g.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i] == n:
                        break              #handles duplication
            result = g
        return result

def main():
    aa = Solution()
    print aa.permuteUnique()
    return 0

if __name__ == "__main__":
    sys.exit(main())
