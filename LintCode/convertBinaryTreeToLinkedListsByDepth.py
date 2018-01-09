#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
        result = []
        q = [root]
        while q:
            tmp = []
            tmp_l = ListNode(0)
            p = tmp_l
            for n in q:
                p.next = ListNode(n.val)
                p = p.next
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            result.append(tmp_l.next)
            q = tmp
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())