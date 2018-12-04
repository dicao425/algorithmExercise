#!/usr/bin/python
import sys

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    return 4

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        buf4 = ['c'] * 4
        while True:
            curr = min(read4(buf4), n-idx)
            buf[idx: idx+curr] = buf4
            idx += curr
            if curr < 4:
                return idx

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())