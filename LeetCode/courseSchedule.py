#!/usr/bin/python
import sys

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        s2, s1 = zip(*prerequisites)
        root = set(s1)-set(s2)
        if len(root) == 0:
            return False
        all = set(sum(prerequisites, []))
        vi = set([])
        ne = {key: [] for key in all}
        for i in prerequisites:
            ne[i[1]] += i[0],
        stack = list(root)
        import pdb
        pdb.set_trace()
        while stack:
            item = stack.pop()
            if item in vi:
                return False
            else:
                vi.add(item)
            stack += ne.pop(item, [])
        return False if ne else True


def main():
    aa = 1111Solution()
    print aa.canFinish(3, [[2,0], [2,1]])
    return 0

if __name__ == "__main__":
    sys.exit(main())
