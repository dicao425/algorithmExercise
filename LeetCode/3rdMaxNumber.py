#!/usr/bin/python
import sys

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = [float('-inf'), float('-inf'), float('-inf')]
        for i in nums:
            if i not in values:
                if i > values[0]:
                    values = [i, values[0], values[1]]
                elif i > values[1]:
                    values = [values[0], i, values[1]]
                elif i > values[2]:
                    values = [values[0], values[1], i]
        return max(values) if float('-inf') in values else values[-1]

def main():
    aa = Solution()
    print aa.thirdMax()
    return 0

if __name__ == "__main__":
    sys.exit(main())
