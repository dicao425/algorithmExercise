#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        self.result = []
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, ss):
        if len(ss) == len(nums):
            self.result.append(ss[:])
            return
        for n in set(nums)-set(ss):
            ss.append(n)
            self.dfs(nums, ss)
            ss.pop()


class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = []
        stack = [[i] for i in nums]
        while stack:
            last = stack.pop()
            if len(last) == len(nums):
                result.append(last)
                continue
            for n in nums:
                if n not in last:
                    stack.append(last + [n])
        return result

def main():
    aa = Solution()
    print aa.permute([1,2,3])
    aa = Solution2()
    print aa.permute([1, 2, 3])
    return 0

if __name__ == "__main__":
    sys.exit(main())