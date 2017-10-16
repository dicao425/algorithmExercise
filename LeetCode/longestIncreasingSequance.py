#!/usr/bin/python
import sys


class Solution(object):
    def LIS(self, l):
        if not l:
            return 0
        dp = [1] * len(l)
        for i, v in enumerate(l):
            for j in range(i):
                if nums[j] < v:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


def main():
    aa = Solution()
    print aa.LIS([1,2,7,8,3,4,9])
    return 0

if __name__ == "__main__":
    sys.exit(main())