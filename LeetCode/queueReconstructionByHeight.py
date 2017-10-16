#!/usr/bin/python
import sys

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        q = []
        people.sort(key=lambda (h, k): (-h, k))
        for p in people:
            q.insert(p[1], p)
        return q

'''
7,0  7,1  6,1  5,0  5,2  4,4
---
7,0 7,1
7,0  6,1  7,1
5,0  7,0  6,1  7,1
5,0  7,0  5,2  6,1  7,1
5,0  7,0  5,2  6,1  4,4  7,1
从大到小开始插入排列
小的不会影响到大的
'''
def main():
    aa = Solution()
    print aa.reconstructQueue()
    return 0

if __name__ == "__main__":
    sys.exit(main())
