#!/usr/bin/python
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        stack = []
        ret = []
        while stack or root:
            if root:
                ret.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root:
                    root = root.right
        return ",".join(str(e) for e in ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data_arr = [int(e) for e in data.split(",")]
        # print data_arr
        stack = []
        root = TreeNode(data_arr[0])
        stack.append(root)
        for i in range(1, len(data_arr)):
            n = None
            while stack and data_arr[i] > stack[-1].val:
                n = stack.pop()

            if n:
                n.right = TreeNode(data_arr[i])
                stack.append(n.right)
            else:
                n = stack[-1]
                n.left = TreeNode(data_arr[i])
                stack.append(n.left)

        return root

def main():
    tt = TreeNode(6)
    tt.left = TreeNode(4)
    tt.right = TreeNode(9)
    tt.left.left = TreeNode(2)
    tt.left.right = TreeNode(5)
    tt.left.left.left = TreeNode(1)
    tt.left.left.right = TreeNode(3)
    tt.right.left = TreeNode(8)
    tt.right.left.left = TreeNode(7)
    tt.right.right = TreeNode(11)
    tt.right.right.left = TreeNode(10)
    aa = Codec()
    print aa.serialize(tt)
    return 0

if __name__ == "__main__":
    sys.exit(main())