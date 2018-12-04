#!/usr/bin/python
import sys

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        curr = None
        cnt = 0
        for ch in chars:
            if curr is None:
                chars[i] = ch
                curr = ch
                cnt = 1
                i += 1
            else:
                if curr == ch:
                    cnt += 1
                else:
                    if cnt != 1:
                        for c in str(cnt):
                            chars[i] = c
                            i += 1
                    chars[i] = ch
                    curr = ch
                    cnt = 1
                    i += 1
        if curr is not None:
            if cnt > 1:
                for c in str(cnt):
                    chars[i] = c
                    i += 1
        return i

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())