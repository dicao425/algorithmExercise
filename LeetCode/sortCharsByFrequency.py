#!/usr/bin/python
import sys

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        a = [[] for _ in range(len(s)+1)]
        for k in d:
            a[d[k]].append(k)
        for i in range(len(a)-1, -1, -1):
            result += ''.join([i*n for n in a[i]])
        return result

def main():
    aa = Solution()
    print aa.frequencySort()
    return 0

if __name__ == "__main__":
    sys.exit(main())
