class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.result = []
        if root is None:
            return self.result
        self.dfs(root, str(root.val))
        return self.result

    def dfs(self, node, path):
        if node.right is None or node.left is None:
            self.result.append(path)
            return
        if node.left is not None:
            self.dfs(node.left, path + '->' + str(node.left.val))
        if node.right is not None:
            self.dfs(node.right, path + '->' + str(node.right.val))
        return

