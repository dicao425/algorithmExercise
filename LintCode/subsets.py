#!/usr/bin/python
import sys

#!/usr/bin/python
import sys

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        for n in nums:
            result += [i+[n] for i in result]
        return result

class Solution2(object):
    # DFS
    def subsets(self, nums):
        self.result = []
        nums.sort()
        self.dfs(nums, [], 0)
        return self.result

    def dfs(self, nums, sub, idx):
        self.result.append(sub[:])
        for i in range(idx, len(nums)):
            self.dfs(nums, sub+nums[i], i+1)

class Solution3(object):
    # Iterate
    def subsets(self, nums):
        result = []
        if not nums:
            return result
        result.append([])
        for n in nums:
            old = [item[:] for item in result]
            for i in result:
                i.append(n)
            result = old + result
        return result


def main():
    aa = Solution()
    print aa.subsets([1,2,3])

    aa = Solution2()
    print aa.subsets([1, 2, 3])

    aa = Solution3()
    print aa.subsets([1, 2, 3])
    return 0

if __name__ == "__main__":
    sys.exit(main())



