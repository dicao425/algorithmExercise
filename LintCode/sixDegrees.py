#!/usr/bin/python
import sys

"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        # write your code here
        result = 0
        if s == t:
            return 0
        q = [(s, 0)]
        visited = {s}
        while q:
            node, step = q.pop(0)
            for n in node.neighbors:
                if n in visited:
                    continue
                if n == t:
                    return step + 1
                q.append((n, step + 1))
                visited.add(n)
        return -1


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())