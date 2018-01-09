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
            if ss not in self.result:
                self.result.append(ss[:])
            return
        temp = nums[:]
        map(temp.remove, ss)
        for n in temp:
            self.dfs(nums, ss+[n])


class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = []
        stack = [[n] for n in nums]
        while stack:
            last = stack.pop()
            if len(last) == len(nums) and last not in result:
                result.append(last)
                continue
            tmp = nums[:]
            map(tmp.remove, last)
            for i in tmp:
                stack.append(last + [i])
        return result

def main():
    aa = Solution()
    print aa.permute([1,2,2])
    print aa.permute([3, 3, 1, 2, 3, 2, 3, 1])
    print "--------"
    aa = Solution2()
    print aa.permute([1, 2, 2])
    print aa.permute([3, 3, 1, 2, 3, 2, 3, 1])
    return 0

if __name__ == "__main__":
    sys.exit(main())