#!/usr/bin/python
import sys


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        self.helper(stack1, S)
        self.helper(stack2, T)
        return stack1 == stack2

    def helper(self, stack, l):
        for item in l:
            if item == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(item)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())