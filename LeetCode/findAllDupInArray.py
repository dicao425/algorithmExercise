#!/usr/bin/python
import sys

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = set()
        result = []
        for n in nums:
            if n in d:
                result.append(n)
            else:
                d.add(n)
        return result

def main():
    aa = Solution()
    print aa.findDuplicates([4,3,2,7,8,2,3,1])
    return 0

if __name__ == "__main__":
    sys.exit(main())
