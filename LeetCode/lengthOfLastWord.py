#!/usr/bin/python
import sys

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])

def main():
    aa = Solution()
    print aa.lengthOfLastWord()
    return 0

if __name__ == "__main__":
    sys.exit(main())
