#!/usr/bin/python
import sys


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        if not S:
            return ''
        l = len(S)
        groups = l / K
        rest = l % K
        start = 0
        result = []
        if rest != 0:
            result.append(S[:rest])
            start = rest
        else:
            groups -= 1
            result.append(S[:K])
            start = K
        while groups:
            result.append(S[start: start + K])
            groups -= 1
            start += K
        return '-'.join(result)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())