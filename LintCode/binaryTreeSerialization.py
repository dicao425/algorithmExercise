#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        def dfs(node):
            if not node:
                self.result.append('#')
                return
            self.result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        self.result = []
        dfs(root)
        return ','.join(self.result)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
        def get_next():
            for i in self.data:
                yield i

        def dfs(data):
            if data == '#':
                return
            root = TreeNode(int(data))
            root.left = dfs(self.d.next())
            root.right = dfs(self.d.next())
            return root

        self.data = data.split(',')
        self.d = get_next()
        return dfs(self.d.next())


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())