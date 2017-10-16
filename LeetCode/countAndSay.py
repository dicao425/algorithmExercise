#!/usr/bin/python
import sys


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        if n == 1:
            return "1"
        num = self.countAndSay(n - 1)
        curr = num[0]
        c = 0
        result = ""
        for i in num:
            if i == curr:
                c += 1
            else:
                result += "%d%s" % (c, curr)
                curr = i
                c = 1
        result += "%d%s" % (c, curr)
        return result
    def countAndSay1(self, n):
        if n == 0:
            return ""
        i = 1
        s = "1"
        while i < n:
            pre = None
            c = 0
            tmp = ""
            for k in s:
                if pre is None:
                    pre = k
                    c = 1
                    continue
                if k == pre:
                    c += 1
                else:
                    tmp += str(c) + pre
                    pre = k
                    c = 1
            if pre and c:
                tmp += str(c) + pre
            s = tmp
            i += 1
        return s
def main():
    aa = Solution()
    print aa.countAndSay(10)
    print aa.countAndSay1(1)
    return 0

if __name__ == "__main__":
    sys.exit(main())
