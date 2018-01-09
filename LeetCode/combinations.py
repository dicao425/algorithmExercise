#!/usr/bin/python
import sys


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:         # need k-l numbers, if n+1-k (k is over the n), no number left, continue to pop the previous one (backtrack)
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

def main():
    aa = Solution()
    print aa.combine(5, 2)
    return 0

if __name__ == "__main__":
    sys.exit(main())