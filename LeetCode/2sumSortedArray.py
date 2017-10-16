#!/usr/bin/python
import sys

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]
        return

def main():
    aa = Solution()
    print aa.twoSum([2,7,11,15], 9)
    return 0

if __name__ == "__main__":
    sys.exit(main())
