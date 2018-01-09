#!/usr/bin/python
import sys

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        q = [node]
        visited = set()
        while q:
            n = q.pop(0)
            if n in visited:
                continue
            else:
                visited.add(n)
            if values[n] == target:
                return n
            q = q + n.neighbors
        return

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())