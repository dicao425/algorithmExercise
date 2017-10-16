#!/usr/bin/python
import sys


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            else:
                if not stack or stack.pop() != d[i]:
                    return False
        if stack:
            return False
        return True


def main():
    aa = Solution()
    print aa.isValid()
    return 0

if __name__ == "__main__":
    sys.exit(main())
