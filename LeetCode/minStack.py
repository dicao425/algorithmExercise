#!/usr/bin/python
import sys


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            m = x
        else:
            m = min(self.stack[-1], x)
        self.stack.append(x)
        self.stack.append(m)

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-2] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1]

def main():
    aa = Solution()
    print aa.MinStack()
    return 0

if __name__ == "__main__":
    sys.exit(main())
