#!/usr/bin/python
import sys

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ('a', 'e', 'i', 'o', 'u')
        f = 0
        l = len(s)-1
        result = list(s)
        while f<l:
            if result[f].lower() not in v:
                f += 1
                continue
            if result[l].lower() not in v:
                l -= 1
                continue
            result[f], result[l] = result[l], result[f]
            f += 1
            l -= 1
        return ''.join(result)

def main():
    aa = Solution()
    print aa.reverseVowels()
    return 0

if __name__ == "__main__":
    sys.exit(main())
