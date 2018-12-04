#!/usr/bin/python
import sys

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = 0
        r = len(arr) - k
        while l < r:
            m = (l+r) / 2
            if x - arr[m] > arr[m+k] - x:
                l = m + 1
            else:
                r = m
        return arr[l: l+k]

class Solution1(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return []
        first = 0
        last = len(arr) - 1
        while first + 1 < last:
            m = (first + last) / 2
            if arr[m] == x:
                first = m
            elif arr[m] < x:
                first = m
            else:
                last = m
        last = first
        while last - first < k:
            if first == 0:
                return arr[:k]
            if last == len(arr):
                return arr[-k:]
            if x - arr[first - 1] <= arr[last] - x:
                first -= 1
            else:
                last += 1
        return arr[first: last]



def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())