#!/usr/bin/python
import sys


class Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
        first = 1
        last = max(L)
        while first + 1 < last:
            m = (first + last) / 2
            pieces = sum([l / m for l in L])
            if pieces >= k:
                first = m
            else:
                last = m
        if sum([l / last for l in L]) >= k:
            return last
        return first

# T(N) = T(N/2) + O(N) = T(N/4) + O(N/2) + O(N) = ... = O(N+N/2+N/4+...+2+1) = O(2N-1) = O(N)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())