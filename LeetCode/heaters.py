#!/usr/bin/python
import sys

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        ans, i = 0, 0
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            dis = min(house-heaters[i], heaters[i+1]-house)
            ans = max(dis, ans)
        return ans

def main():
    aa = Solution()
    print aa.findRadius()
    return 0

if __name__ == "__main__":
    sys.exit(main())
