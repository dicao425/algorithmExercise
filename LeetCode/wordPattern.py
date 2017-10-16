#!/usr/bin/python
import sys

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #return len(set(zip(pattern, str.strip().split(' ')))) == len(set(list(pattern))) and len(set(str.strip().split(' '))) == len(set(list(pattern))) and len(str.strip().split(' ')) == len(pattern)
        return self.check(list(pattern)) == self.check(str.split())
    def check(self, s):
        d = {}
        for i, v in enumerate(s):
            if v not in d:
                d[v] = [i]
            else:
                d[v].append(i)
        return sorted(d.values())

def main():
    aa = Solution()
    print aa.wordPattern()
    return 0

if __name__ == "__main__":
    sys.exit(main())
