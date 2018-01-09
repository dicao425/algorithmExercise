#!/usr/bin/python
import sys

class Solution:
    """
    @param: key: A string you should hash
    @param: HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for k in key:
            ans = (ans * 33 + ord(k)) % HASH_SIZE
        return ans

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())