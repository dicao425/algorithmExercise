#!/usr/bin/python
import sys


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = list(s)
        for i in range(0, len(s), 2 * k):
            result[i:i + k] = reversed(s[i:i + k])
        return "".join(result)

def main():
    aa = Solution()
    print aa.reverseStr("abcdefg")
    return 0

if __name__ == "__main__":
    sys.exit(main())
