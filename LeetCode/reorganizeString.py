#!/usr/bin/python
import sys

import collections


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        length = len(S)
        new_list = []
        for c, num in sorted(collections.Counter(S).items(), key=lambda x: -x[1]):
            if num > (length + 1) / 2:
                return ""
            new_list += [c] * num
        result = [None] * length
        result[::2] = new_list[:(length + 1) / 2]
        result[1::2] = new_list[(length + 1) / 2:]
        return ''.join(result)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())