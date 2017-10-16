#!/usr/bin/python
import sys

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):  # 32bits 4bits-1
            n = num & 15       # this means num & 1111b qu zheng
            c = mp[n]          # get the hex char
            ans = c + ans
            num = num >> 4      # qu yu
        return ans.lstrip('0')  #strip leading zeroes

def main():
    aa = Solution()
    print aa.toHex()
    return 0

if __name__ == "__main__":
    sys.exit(main())
