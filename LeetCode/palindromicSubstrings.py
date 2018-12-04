#!/usr/bin/python
import sys

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                if s[i: j] == s[i: j][::-1]:
                    result += 1
        return result
# Best solution is O(n)
# Manacher's Algorithm
    def countSubstringsM(self, S):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in xrange(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v + 1) / 2 for v in manachers(S))

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())