#!/usr/bin/python
import sys

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0] * length
        for s, e, v in updates:
            result[s] += v  # indicate the position to start increasement;
            if e < length - 1:
                result[e+1] -= v    # indicate the pos to cancel the increasement;
        pre = 0
        for i in range(length):
            result[i] += pre
            pre = result[i]
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())