#!/usr/bin/python
import sys

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        visited = {}
        visited[root.label] = root
        stack = [node]
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.label not in visited:
                    visited[n.label] = UndirectedGraphNode(n.label)
                    stack.append(n)
                visited[top.label].neighbors.append(visited[n.label])
        return root

def main():
    aa = Solution()
    print aa.cloneGraph()
    return 0

if __name__ == "__main__":
    sys.exit(main())
