#!/usr/bin/python
import sys


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jd = set(J)
        result = 0
        for s in S:
            if s in jd:
                result += 1
        return result


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())