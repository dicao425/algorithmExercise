#!/usr/bin/python
import sys

# Segment Tree   O(logN)
#self.c[1] = nums[0]

#self.c[2] = nums[0] + nums[1]

#self.c[3] = nums[2]

#self.c[4] = nums[0] + nums[1] + nums[2] + nums[3]

#self.c[5] = nums[4]

#self.c[6] = nums[4] + nums[5]

#self.c[7] = nums[6]

#self.c[8] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]

'''
k += k & -k      叫 'lowbit'
末尾0的个数  构建时
0 - 0 = ---
1 - 1 = 0
2 - 10 = 1
3 - 11 = 0
4 - 100 = 2
5 - 101 = 0
6 - 110 = 1
7 - 111 = 0
8 - 1000 = 3
...
2^k 依次放好

sum 时 依次去除末尾的1， 依次相加
ex：
sum 7 就是 c7 (111) + c6 (110) + c4 (100) + 0 = n6 + n4+n5 + n0+n1+n2+n3


范围sum的话就是 i=2  j=6  --> sum (6+1) - sum (2)


更新：找到那些只有目标元素的项，挨个更新即可
'''


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.c = [0] * (len(nums) + 1)
        self.nums = nums
        for i in range(len(self.nums)):
            k = i + 1
            while k <= len(self.nums):
                self.c[k] += self.nums[i]
                k += k & -k

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= len(self.nums):
            self.c[i] += diff
            i += i & -i

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        result = 0
        j += 1
        while j:
            result += self.c[j]
            j -= j & -j
        while i:
            result -= self.c[i]
            i -= i & -i
        return result


# Simple way   O(n)

class NumArray1(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.l = [0] * len(nums)
        self.nums = nums
        for i, n in enumerate(nums):
            self.l[i] = (self.l[i-1] if i != 0 else 0) + n


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        for k in xrange(i, len(self.nums)):
            self.l[k] = self.l[k] - self.nums[i] + val
        self.nums[i] = val


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.l[j] - (self.l[i-1] if i != 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

def main():
    aa = NumArray()
    return 0

if __name__ == "__main__":
    sys.exit(main())
