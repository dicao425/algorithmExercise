#!/usr/bin/python
import sys

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        p = path.split("/")
        new = []
        for i in p:
            if not i or i == ".":
                continue
            elif i == "..":
                if new:
                    new.pop()
            else:
                new.append(i)
        return '/'+'/'.join(new)

def main():
    aa = Solution()
    print aa.simplifyPath()
    return 0

if __name__ == "__main__":
    sys.exit(main())
