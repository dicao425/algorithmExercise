#!/usr/bin/python
import sys

class Solution:
    """
    @param: s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        i = 0
        j = len(s)-1
        while i<j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())