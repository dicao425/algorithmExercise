#!/usr/bin/python
import sys


class Find(object):
    def solve(self, e):
        s1, s2 = zip(*e)
        root = set(s1)-set(s2)
        if len(root) != 1:
            return False
        all = set(sum(e, []))
        vi = set([])
        ne = {key: [] for key in all}
        for i, j in e:
            ne[i] += j,
        stack = [root.pop()]
        while stack:
            item = stack.pop()
            if item in vi:
                return False
            else:
                vi.add(item)
            stack += ne.pop(item, [])
        return False if ne else True


def main():
    aa = Find()
    print aa.solve([
        ['A','B'],
        ['A', 'C'],
        ['B', 'D'],
        ['M', 'E']
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())
