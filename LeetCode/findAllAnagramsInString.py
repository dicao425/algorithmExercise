#!/usr/bin/python
import sys


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lp = len(p)
        ls = len(s)
        result = []
        d = {}
        for i in p:
            d[i] = d.get(i, 0) + 1
        td = d.copy()
        i = 0
        b = -1
        while i < ls:
            if set(td.values()) == set([0]):
                result.append(i-lp)
            if s[i] not in td:
                b = i
                i += 1
                td = d.copy()
                continue
            td[s[i]] -= 1
            if i-lp > b:
                td[s[i-lp]] += 1
            i += 1
        if set(td.values()) == set([0]):
            result.append(i-lp)
        return result


def main():
    aa = Solution()
    print aa.findAnagrams('aaaaaaaa', 'a')
    print aa.findAnagrams('abab', 'ab')
    print aa.findAnagrams('cbaebabacd', 'abc')
    return 0

if __name__ == "__main__":
    sys.exit(main())
