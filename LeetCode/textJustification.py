#!/usr/bin/python
import sys


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        curr = []
        result = []
        curr_len = 0
        for w in words:
            if len(w) + len(curr) + curr_len > maxWidth:
                for i in range(maxWidth - curr_len):
                    curr[i % (len(curr) - 1 if len(curr) != 1 else 1)] += ' '
                result.append(''.join(curr))
                curr = []
                curr_len = 0
            curr += [w]
            curr_len += len(w)
        return result + [' '.join(curr).ljust(maxWidth)]


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())