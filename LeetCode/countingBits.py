#!/usr/bin/python
import sys

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]*(num+1)
        for i in range(num+1):
            result[i] = result[i>>1] + i&1
        return result

def main():
    aa = Solution()
    print aa.countBits()
    return 0

if __name__ == "__main__":
    sys.exit(main())
