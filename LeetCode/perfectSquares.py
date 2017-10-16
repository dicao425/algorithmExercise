#!/usr/bin/python
import sys
'''
As I wrote, the algorithm is Breadth First Search (BFS). Imagine that you have a graph where vertices are numbers from
0 to n. 2 vertices are connected dirrectly if their values are different by a square number. for example:
1 and 2 connected, 2 and 3 connected, 2 and 6 connected, 2 and 11 connected, 1 and 5 connected, 1 and 10 connected, etc.

So starting from vertex 0, you look for the vertex n by BFS. The distance is exactly what we need to return.
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        edges = [i*i for i in range(1, int(n**0.5)+1)]
        visited = [False] * (n+1)
        step = 0
        ends = [0]
        while True:
            step += 1
            starts = ends
            ends = []
            for start in starts:
                for edge in edges:
                    end = start + edge
                    if end == n:
                        return step
                    if end > n:
                        break
                    if visited[end]:
                        continue
                    visited[end] = True
                    ends.append(end)
        return

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())