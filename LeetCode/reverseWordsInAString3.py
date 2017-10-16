#!/usr/bin/python
import sys

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([i[::-1] for i in s.split(' ')])

def main():
    aa = Solution()
    print aa.reverseWords()
    return 0

if __name__ == "__main__":
    sys.exit(main())
