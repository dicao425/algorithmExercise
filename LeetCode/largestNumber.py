#!/usr/bin/python
import sys

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = [str(i) for i in nums]
        num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        result = ''.join(num).lstrip('0')
        if not result:
            return '0'
        else:
            return result

def main():
    aa = Solution()
    print aa.largestNumber()
    return 0

if __name__ == "__main__":
    sys.exit(main())
