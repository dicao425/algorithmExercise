#!/usr/bin/python
import sys
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        if not nums:
            self.result.append(path)
            return
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]])

def main():
    aa = Solution()
    print aa.permute()
    return 0

if __name__ == "__main__":
    sys.exit(main())
