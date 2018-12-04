#!/usr/bin/python
import sys


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters:
            return
        l = 0
        r = len(letters) - 1
        t = ord(target)
        while l + 1 < r:
            m = (l + r) / 2
            if ord(letters[m]) < t:
                l = m
            elif ord(letters[m]) > t:
                r = m
            else:
                l = m
        if l < len(letters) and ord(letters[l]) > t:
            return letters[l]
        if r < len(letters) and ord(letters[r]) > t:
            return letters[r]
        return letters[0]


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())