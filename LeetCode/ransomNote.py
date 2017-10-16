#!/usr/bin/python
import sys

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt = collections.Counter(magazine)
        for letter in ransomNote:
            if letter not in cnt:
                return False
            cnt[letter] -= 1
            if cnt[letter] < 0:
                return False
        return True

def main():
    aa = Solution()
    print aa.canConstruct("a", "ab")
    return 0

if __name__ == "__main__":
    sys.exit(main())
