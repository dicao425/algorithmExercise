#!/usr/bin/python
import sys


def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for i in tokens:
        if i not in ('+', '-', '*', '/'):
            stack.append(int(i))
        else:
            stack.append(self.oper(stack.pop(), stack.pop(), i))
    return stack[0]


def oper(self, a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return b - a
    elif op == '*':
        return a * b
    elif op == '/':
        return int(b / float(a))

def main():
    tokens = ["4", "13", "5", "/", "+"]
    aa = Solution()
    print aa.eval(tokens)
    return 0

if __name__ == "__main__":
    sys.exit(main())