#!/usr/bin/python
import sys

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        l = len(s)
        if l == 0:
            return False
        i = 0
        dot = False
        E = False
        has_digit = False
        has_sign = False
        while i < l:
            if s[i].isdigit():
                i += 1
                has_digit = True
                has_sign = True
            elif not dot and s[i] == '.':
                i += 1
                dot = True
                has_sign = True
            elif has_digit and not E and s[i] in ('E', 'e'):
                i += 1
                dot = True
                E = True
                has_digit = False
                has_sign = False
            elif not has_digit and not has_sign and s[i] in ('+', '-'):
                i += 1
                has_sign = True
            else:
                return False
        if has_digit:
            return True
        return False


# DFA
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define a DFA
        state = [{},
              {'blank': 1, 'sign': 2, 'digit':3, '.':4},
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())