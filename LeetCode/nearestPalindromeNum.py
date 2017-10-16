#!/usr/bin/python
import sys

class Solution(object):
    def nearestPalindromeNum(self, nums):
        if not nums:
            return []
        length = len(nums)
        mid = length / 2
        if self.isPal(nums):
            if set(nums) == set(['9']):
                return self.all9(nums)
            else:
                return self.nearest(nums, self.generate(self.op(nums, 1)), self.generate(self.op(nums, -1)))
        else:
            tmp = self.generate(nums)
            if int(''.join(tmp)) < int(''.join(nums)):
                return self.nearest(nums, self.generate(self.op(nums, 1)), tmp)
            else:
                return self.nearest(nums, tmp, self.generate(self.op(nums, -1)))

    def generate(self, nums):
        l = len(nums)
        tn = nums[:]
        i = l/2-1
        j = l/2 if l%2 == 0 else l/2+1
        while i>-1:
            tn[j] = tn[i]
            i -= 1
            j += 1
        return tn

    def isPal(self, nums):
        l = len(nums)
        i = l / 2 - 1
        j = l / 2 if l % 2 == 0 else l / 2 + 1
        while i > -1:
            if nums[i] != nums[j]:
                return False
            i -= 1
            j += 1
        return True

    def all9(self, nums):
        l = len(nums)
        nums = ['0'] * l
        nums[0] = '1'
        nums.append('1')
        return nums

    def op(self, nums, p):
        l = len(nums)
        mid = l / 2 - 1
        if mid<0:
            return [str(int(nums[0])+p)]
        tn = nums[:]
        for i in range(mid, -1, -1):
            tmp = str((int(tn[i])+p)%10)
            p = (int(tn[i]) + p) // 10
            tn[i] = tmp
        return tn

    def nearest(self, nums, numsA, numsB):
        n = int(''.join(nums))
        nA = int(''.join(numsA))
        nB = int(''.join(numsB))
        return numsA if abs(n-nA) < abs(n-nB) else numsB

def main():
    mm = ['1','2','3','4','5','6','7','8']
    mm1 = ['1', '2', '3', '4', '9', '9', '9', '9']
    mm = ['9', '9', '9', '9', '9', '9', '9', '9']
    mm = ['1', '1']
    mm = ['2']
    mm = ['9','4','1','8','7','9','7','8','3','2','2']
    mm=[]
    mm = ['1','2','3']
    aa = Solution()
    print aa.nearestPalindromeNum(mm)
    return 0

if __name__ == "__main__":
    sys.exit(main())