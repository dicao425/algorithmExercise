#!/usr/bin/python
import sys

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for i in employees:
            d[i.id] = (i.importance, i.subordinates)
        stack = [id]
        visited = set()
        result = 0
        while stack:
            c = stack.pop()
            if c in visited:
                continue
            visited.add(c)
            result += d[c][0]
            stack += d[c][1]
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())