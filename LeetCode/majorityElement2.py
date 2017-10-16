#!/usr/bin/python
import sys
import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = collections.Counter()
        for n in nums:
            c[n] += 1
            if len(c) == 3:
                c -= collections.Counter(set(c))
                # c Counter({1: 2, 2: 1, 3: 1})
                # set(c) = set(1,2,3)
                # c -= co...Counter(set(c))  --> Counter({1:1})
                # Cut all by 1
        c = collections.Counter([n for n in nums if n in c])
        return [i for i in c if c[i]>len(nums)/3]

def main():
    aa = Solution()
    print aa.majorityElement()
    return 0

if __name__ == "__main__":
    sys.exit(main())
