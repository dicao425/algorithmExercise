#!/usr/bin/python
import sys

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegree = {}
        for n in graph:
            if n not in indegree:
                indegree[n] = 0
            for i in n.neighbors:
                indegree[i] = indegree.get(i, 0) + 1
        q = []
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        if not q:
            return []
        result = []
        while q:
            node = q.pop(0)
            result.append(node)
            for n in node.neighbors:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())