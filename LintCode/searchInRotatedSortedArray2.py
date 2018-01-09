#!/usr/bin/python
import sys

class Solution:
    """
    @param: A: an integer ratated sorted array and duplicates are allowed
    @param: target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return False
        for n in A:
            if n == target:
                return True
        return False

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())