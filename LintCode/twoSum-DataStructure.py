#!/usr/bin/python
import sys


class TwoSum:
    """
    @param: number: An integer
    @return: nothing
    """

    def __init__(self):
        self.h = {}

    def add(self, number):
        # write your code here
        self.h[number] = self.h.get(number, 0) + 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for n in self.h:
            t = value - n
            if t in self.h and (t != n or self.h[t] > 1):
                return True
        return False


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())