#!/usr/bin/python
import sys

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = dp[1] = 1
        for i in range(2, len(s)+1):
            if int(s[i-2: i]) > 10 and int(s[i-2: i]) <= 26 and s[i-1] != '0':
                dp[i] = dp[i-2] + dp[i-1]
            elif int(s[i-2: i]) == 10 or int(s[i-2: i]) == 20:
                dp[i] = dp[i-2]
            elif int(s[i-1]) != 0:
                dp[i] = dp[i-1]
            else:
                return 0
        return dp[-1]

def main():
    aa = Solution()
    print aa.numDecodings("12120")
    return 0

if __name__ == "__main__":
    sys.exit(main())