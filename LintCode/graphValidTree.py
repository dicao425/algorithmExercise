#!/usr/bin/python
import sys


class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
        if len(edges) != n-1:
            return False
        g = {}
        for e in edges:
            g[e[0]] = g.get(e[0], []) + [e[1]]
            g[e[1]] = g.get(e[1], []) + [e[0]]
        q = [0]
        visited = {0}
        while q:
            node = q.pop(0)
            for i in g.get(node, []):
                if i in visited:
                    continue
                q.append(i)
                visited.add(i)
        return len(visited) == n

    def validTree1(self, n, edges):
        # write your code here
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False
        g = {}
        for e in edges:
            g[e[0]] = g.get(e[0], []) + [e[1]]
            g[e[1]] = g.get(e[1], []) + [e[0]]
        q = [0]
        while q:
            q += g.pop(q.pop(0), [])
        return not g

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())