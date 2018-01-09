#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        nl = [(0, -1)]
        s = 0
        for i, num in enumerate(nums):
            s += num
            nl.append((s, i))
        nl = sorted(nl, key=lambda x: x[0])
        results = [0, 0]
        ans = float('inf')
        for i in range(len(nl)-1):
            if nl[i+1][0] - nl[i][0] < ans or nl[i+1][0] - nl[i][0] == ans and min(nl[i+1][1], nl[i][1]) + 1 < results[0]:
                ans = nl[i+1][0] - nl[i][0]
                results[0] = min(nl[i+1][1], nl[i][1]) + 1
                results[1] = max(nl[i+1][1], nl[i][1])
        return results

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())