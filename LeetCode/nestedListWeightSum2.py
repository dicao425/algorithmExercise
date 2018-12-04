#!/usr/bin/python
import sys


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        root = [n for n in nestedList]
        result = 0
        tmp = 0
        while root:
            new_root = []
            for item in root:
                if item.isInteger():
                    tmp += item.getInteger()
                else:
                    for i in item.getList():
                        new_root.append(i)
            root = new_root
            result += tmp
        return result

'''
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        weighted, unweighted = 0, 0
        while nestedList:
            nextLevel = []
            for item in nestedList:
                if item.isInteger():
                    unweighted += item.getInteger()
                else:
                    nextLevel += item.getList()
            weighted += unweighted
            nestedList = nextLevel
        return weighted'''
def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())