#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def BFSQlevelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        q = [(0, root)]
        while q:
            item = q.pop(0)
            if item[1]:
                if len(result) < item[0] + 1:
                    result.insert(0, [])
                result[-(item[0] + 1)].append(item[1].val)
                q.append((item[0] + 1, item[1].left))
                q.append((item[0] + 1, item[1].right))
        return result

    def DFSSlevelOrderBottom(self, root):
        result = []
        s = [(0, root)]
        while s:
            l, node = s.pop()
            if node:
                if len(result) < l + 1:
                    result.insert(0, [])
                result[-(l + 1)].append(node.val)
                s.append((l + 1, node.right))
                s.append((l + 1, node.left))
        return result

    def levelOrderBottom(self, root):
        self.result = []
        self.dfs(0, root)
        return self.result

    def dfs(self, l, node):
        if node:
            if len(self.result) < l + 1:
                self.result.insert(0, [])
            self.result[-(l + 1)].append(node.val)
            self.dfs(l + 1, node.left)
            self.dfs(l + 1, node.right)


def main():
    aa = Solution()
    print aa.levelOrderBottom()
    return 0

if __name__ == "__main__":
    sys.exit(main())
