#!/usr/bin/python
import sys

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        result = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            else:
                result = max(result, i-start+1)
            d[s[i]] = i
        return result

def main():
    aa = Solution()
    print aa.lengthOfLongestSubstring()
    return 0

if __name__ == "__main__":
    sys.exit(main())
