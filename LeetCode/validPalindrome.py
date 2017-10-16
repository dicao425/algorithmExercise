#!/usr/bin/python
import sys

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ns = "".join([i.lower() for i in s if i.isalnum()])
        return ns == ns[::-1]

def main():
    aa = Solution()
    print aa.isPalindrome()
    return 0

if __name__ == "__main__":
    sys.exit(main())
