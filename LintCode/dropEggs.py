#!/usr/bin/python
import sys
class Solution:
    """
    @param: n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        # write your code here
        # sqrt n  O(√n)
        x = 0
        result = 0
        while result < n:
            x += 1
            result += x
        return x

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())