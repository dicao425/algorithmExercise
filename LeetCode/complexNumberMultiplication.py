#!/usr/bin/python
import sys

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        return "{0}+{1}i".format(a1*b1-a2*b2, a1*b2+a2*b1)

def main():
    aa = Solution()
    print aa.complexNumberMultiply()
    return 0

if __name__ == "__main__":
    sys.exit(main())
