#!/usr/bin/python
import sys

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        s = set()
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                s.add(i)
                s.add(num/i)
        if num in s:
            s.remove(num)
        return num == sum(s)

def main():
    aa = Solution()
    print aa.checkPerfectNumber(28)
    return 0

if __name__ == "__main__":
    sys.exit(main())
