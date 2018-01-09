#!/usr/bin/python
import sys

class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        d = {}
        for i, n in enumerate(numbers):
            if target - n in d:
                return [d[target-n], i]
            d[n] = i
        return []

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())