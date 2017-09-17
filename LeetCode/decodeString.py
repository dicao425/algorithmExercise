#!/usr/bin/python
import sys


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns = []
        cs = []
        if not s:
            return ""
        i = 0
        result = ""
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ns.append(num)
                continue
            elif s[i] == '[':
                cs.append("")
                i += 1
                continue
            elif s[i] == ']':
                n = ns.pop()
                c = cs.pop()
                r = c * n
                if not ns and not cs:
                    result += r
                else:
                    cs[-1] += r
                i += 1
            else:
                if cs:
                    cs[-1] += s[i]
                else:
                    result += s[i]
                i += 1
        return result

def main():
    aa = Solution()
    print aa.decodeString("2[abc]3[cd]ef")
    return 0

if __name__ == "__main__":
    sys.exit(main())