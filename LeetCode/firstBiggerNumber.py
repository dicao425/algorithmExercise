#!/usr/bin/python
import sys


class Solution(object):
    def first_bigger_number(self, nums):
        if not nums:
            return []
        stack = []
        for i, v in enumerate(nums):
            if not stack:
                stack.append(i)
            else:
                pre_i = stack.pop()
                while v > nums[pre_i]:
                    nums[pre_i] = v
                    if stack:
                        pre_i = stack.pop()
                    else:
                        pre_i = i
                if pre_i != i:
                    stack.append(pre_i)
                stack.append(i)
        if stack:
            while stack:
                nums[stack.pop()] = -1
        return nums

def main():
    aa = Solution()
    print aa.first_bigger_number([1,3,2,4,1])
    return 0

if __name__ == "__main__":
    sys.exit(main())
