#!/usr/bin/python
import sys

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return sorted(nums)[len(nums)/2]
        result = nums[0]
        count = 0
        for n in nums:
            if count == 0:
                result = n
                count += 1
            elif n != result:
                count -= 1
            else:
                count += 1
        return result

def main():
    aa = Solution()
    print aa.majorityElement()
    return 0

if __name__ == "__main__":
    sys.exit(main())
