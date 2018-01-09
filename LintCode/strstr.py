#!/usr/bin/python
import sys


class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        for i in range(len(source)-len(target)+1):
            if source[i: i+len(target)] == target:
                return i
        return -1

# write your code here

def main():
    aa = Solution()
    print aa.strStr("","")
    print aa.strStr(" ", " ")
    print aa.strStr("asdfasdf", "eee")
    print aa.strStr("asdfsadgfasdf", "dg")
    print aa.strStr("addssee", "s")
    print aa.strStr("abcdabcdefg", "bcd")
    return 0

if __name__ == "__main__":
    sys.exit(main())

