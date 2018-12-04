#!/usr/bin/python
import sys

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10 and five:
                five -= 1
                ten += 1
            elif b == 20 and ten and five:
                five -= 1
                ten -= 1
            elif b == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())