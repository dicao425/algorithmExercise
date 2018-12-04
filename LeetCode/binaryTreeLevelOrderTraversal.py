#!/usr/bin/python
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [(root, 0)]
        result = []
        while q:
            node, level = q.pop(0)
            if len(result) < level+1:
                result.append([])
            result[level].append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return result


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, node, level):
        if not node:
            return
        if level < len(self.result):
            self.result[level].append(node.val)
        else:
            self.result.append([node.val])
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())