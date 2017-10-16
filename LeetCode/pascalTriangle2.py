#!/usr/bin/python
import sys


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(rowIndex+1):
            if len(result) <= i:
                result.append(1)
            for j in range(i-1, 0, -1):
                result[j] = result[j-1] + result[j]
        return result


def main():
    aa = Solution()
    print aa.getRow()
    return 0

if __name__ == "__main__":
    sys.exit(main())
