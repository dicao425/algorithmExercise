#!/usr/bin/python
import sys

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        p = range(n)
        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]
        for v, w in edges:
            p[find(v)] = p[find(w)]
        result = map(find, p)
        return len(set(result))

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())