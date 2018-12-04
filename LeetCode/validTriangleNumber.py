#!/usr/bin/python
import sys


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        result = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    result += k - j
                    j += 1
                else:
                    k -= 1
        return result



def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())