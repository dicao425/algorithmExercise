#!/usr/bin/python
import sys
class Solution(object):
    def isMatching(self, s, p):
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        dp[0][0] = True
        for i in range(2, len(p)+1):
            dp[i][0] = dp[i-2][0] and p[i-1] == '*'
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j]
                    if p[i-2] == '.' or p[i-2] == s[j-1]:
                        dp[i][j] = dp[i][j-1] or dp[i][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and p[i-1] == s[j-1]
        return dp[-1][-1]

def main():
    aa = Solution()
    print aa.isMatching("aab", "c*a*b")
    return 0

if __name__ == "__main__":
    sys.exit(main())