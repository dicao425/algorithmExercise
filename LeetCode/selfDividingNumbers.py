#!/usr/bin/python
import sys

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            n = i
            while n:
                r = n % 10
                if r == 0 or i % r:
                    break
                n = n / 10
            else:
                result.append(i)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())