#!/usr/bin/python
import sys

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())