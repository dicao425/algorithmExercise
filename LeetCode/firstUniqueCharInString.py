#!/usr/bin/python
import sys

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        d = {}
        for i, l in enumerate(s):
            if l in d:
                d[l].append(i)
            else:
                d[l] = [i]
        for l in s:
            if len(d[l]) == 1:
                return d[l][0]
        return -1


#One time pass the string (another traverse is map)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        m = {chr(k):[] for k in range(97,123)}
        for i, l in enumerate(s):
            m[l].append(i)
        result = None
        for k, v in m.items():
            if len(v) == 1:
                if result is None:
                    result = v[0]
                else:
                    result = min(result, v[0])
        return result if result is not None else -1

def main():
    aa = Solution()
    print aa.firstUniqChar()
    return 0

if __name__ == "__main__":
    sys.exit(main())
