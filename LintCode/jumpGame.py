#!/usr/bin/python
import sys


class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """

    def canJump1(self, A):
        # write your code here
        # Greedy
        m = 0
        for i, v in enumerate(A):
            if i > m:
                return False
            m = max(m, i + v)
        return True

    def canJump(self, A):
        # write your code here
        # DP
        dp = [False] * len(A)
        dp[0] = True
        for i in range(1, len(A)):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
        return dp[-1]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())