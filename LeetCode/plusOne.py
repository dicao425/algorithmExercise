#!/usr/bin/python
import sys


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        t = 1
        for i in range(len(digits)-1, -1, -1):
            n = digits[i] + t
            if n > 9:
                n = 0
            else:
                t = 0
            result.insert(0, n)
        if t == 1:
            result.insert(0, 1)
        return result

def main():
    aa = Solution()
    print aa.plusOne()
    return 0

if __name__ == "__main__":
    sys.exit(main())
