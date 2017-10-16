#!/usr/bin/python
import sys

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        result = []
        sumidx = float('inf')
        for i, r in enumerate(list1):
            d[r] = i
        for i, r in enumerate(list2):
            if r in d:
                if i + d[r] > sumidx:
                    continue
                elif i + d[r] == sumidx:
                    result.append(r)
                else:
                    result = [r]
                    sumidx = i + d[r]
        return result

def main():
    aa = Solution()
    print aa.findRestaurant()
    return 0

if __name__ == "__main__":
    sys.exit(main())
