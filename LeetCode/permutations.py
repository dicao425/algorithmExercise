#!/usr/bin/python
import sys

# Recursive dfs
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, ss):
        if len(ss) == len(nums):
            self.result.append(ss[:])
            return
        for n in set(nums) - set(ss):
            ss.append(n)
            self.dfs(nums, ss)
            ss.pop()

# Iterate dfs
class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        stack = [[i] for i in nums]
        while stack:
            last = stack.pop()
            if len(last) == len(nums):
                result.append(last)
                continue
            for n in nums:
                if n not in last:
                    candidate = last + [n]
                    if len(candidate) == len(nums):
                        result.append(candidate)
                    else:
                        stack.append(candidate)
        return result


def main():
    aa = Solution()
    print aa.permute()
    return 0

if __name__ == "__main__":
    sys.exit(main())
