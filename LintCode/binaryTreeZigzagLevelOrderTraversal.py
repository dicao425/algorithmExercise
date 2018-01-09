#!/usr/bin/python
import sys
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
        result = []
        q = [(root, 0)]
        while q:
            node, l = q.pop(0)
            if len(result) < l + 1:
                result.append([])
            if l % 2 == 1:
                result[l].append(node.val)
            else:
                result[l].insert(0, node.val)
            if node.right:
                q.append((node.right, l+1))
            if node.left:
                q.append((node.left, l+1))
        return result
def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())