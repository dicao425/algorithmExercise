#!/usr/bin/python
import sys

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = j = 0
        m, n = len(word), len(abbr)
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isdigit():
                k = j
                while k < n and abbr[k].isdigit():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())