#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        nums.sort()
        length = len(nums)
        dp = [1] * length
        pre = [None] * length
        for i in range(length):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j
        idx = dp.index(max(dp))
        ans = []
        while idx is not None:
            ans.append(nums[idx])
            idx = pre[idx]
        return ans

def main():
    aa = Solution()
    print aa.largestDivisibleSubset([1,2,3,4,5,6,7,8])
    return 0

if __name__ == "__main__":
    sys.exit(main())