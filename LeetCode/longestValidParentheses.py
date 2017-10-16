#!/usr/bin/python
import sys


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # push the INDEX into the stack!!!!
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i - last)
                    else:
                        maxlen = max(maxlen, i - stack[len(stack) - 1])
        return maxlen

def main():
    aa = Solution()
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())