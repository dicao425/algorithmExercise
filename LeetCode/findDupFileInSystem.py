#!/usr/bin/python
import sys

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for p in paths:
            path = p.split(" ")[0]
            files = p.split(" ")[1:]
            for f in files:
                con = f[f.index("(") + 1:f.rindex(")")]
                name = f[:f.index("(")]
                d[con] = d.get(con, []) + [os.path.join(path, name)]
        return [i for i in d.values() if len(i) != 1]


def main():
    aa = Solution()
    print aa.findDuplicate()
    return 0

if __name__ == "__main__":
    sys.exit(main())
