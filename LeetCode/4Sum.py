#!/usr/bin/python
import sys

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        result = set()
        d = {}
        nums.sort()
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] not in d:
                    d[nums[i]+nums[j]] = [(i, j)]
                else:
                    d[nums[i]+nums[j]].append((i, j))
        for i in range(length-1):
            for j in range(i+1, length):
                T = target - nums[i] - nums[j]
                if T in d:
                    for item in d[T]:
                        if item[0] > j:
                            result.add((nums[i], nums[j], nums[item[0]], nums[item[1]]))
        return [list(i) for i in result]

def main():
    aa = Solution()
    print aa.fourSum()
    return 0

if __name__ == "__main__":
    sys.exit(main())
