#!/usr/bin/python
import sys


#Definition for a binary tree node.
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
        def dfs(node):
            if node is None:
                self.result.append(None)
                return
            self.result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        self.result = []
        dfs(root)
        return self.result



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def get_n():
            for i in self.data:
                yield i
        def dfs(v):
            if v is None:
                return
            node = TreeNode(v)
            node.left = dfs(self.g.next())
            node.right = dfs(self.g.next())
            return node

        self.data = data
        self.g = get_n()
        return dfs(self.g.next())

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    aa = Codec()
    r1 = aa.serialize(root)
    r2 = aa.deserialize(r1)
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())