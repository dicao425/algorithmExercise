#!/usr/bin/python
import sys
class Solution(object):
    def findTheDifference1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dd = {}
        for i in s:
            if i in dd:
                dd[i] += 1
            else:
                dd[i] = 1
        for j in t:
            if j not in dd:
                return j
            else:
                if dd[j] == 0:
                    return j
                else:
                    dd[j] -= 1
    def findTheDifference(self, s, t):
        cc = 0
        for i in s+t:
            cc ^= ord(i)
        return chr(cc)

def main():
    aa = Solution()
    print aa.findTheDifference("abcd", "abcde")
    return 0

if __name__ == "__main__":
    sys.exit(main())
