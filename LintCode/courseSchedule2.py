#!/usr/bin/python
import sys

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        edges = {i: [] for i in range(numCourses)}
        degree = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edges[j].append(i)
            degree[i] += 1
        q = []
        for n in range(numCourses):
            if degree[n] == 0:
                q.append(n)
        result = []
        while q:
            node = q.pop(0)
            result.append(node)
            for next in edges[node]:
                degree[next] -= 1
                if degree[next] == 0:
                    q.append(next)
        if len(result) == numCourses:
            return result
        return []

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())