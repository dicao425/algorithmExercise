#!/usr/bin/python
import sys


class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        stack = [0]
        while stack:
            print stack
            stack += neighbors.pop(stack.pop(), [])
        return not neighbors
def main():
    aa = Solution()
    print aa.validTree(5, [[0,1],[0,2],[1,3],[3,2]])
    # print aa.validTree(4, [['a', 'b'], ['a', 'c'], ['b', 'd']])
    return 0

if __name__ == "__main__":
    sys.exit(main())