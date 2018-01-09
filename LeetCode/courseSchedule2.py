#!/usr/bin/python
import sys


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        q = []
        for n in range(numCourses):
            if degrees[n] == 0:
                q.append(n)
        result = []
        while q:
            node = q.pop(0)
            result.append(node)
            for next in edges[node]:
                degrees[next] -= 1
                if degrees[next] == 0:
                    q.append(next)
        if len(result) != numCourses:
            return []
        return result


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())