#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1
        first = 0
        last = len(nums)-1
        while first+1 < last:
            m = (first+last)/2
            if nums[m] < nums[m+1]:
                first = m
            elif nums[m] < nums[m-1]:
                last = m
            else:
                last = m
        return max(nums[first], nums[last])

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())