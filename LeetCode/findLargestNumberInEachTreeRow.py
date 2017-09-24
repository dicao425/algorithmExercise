class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        rows = []
        q = [(0, root)]
        while q:
            l, c = q.pop(0)
            if len(rows) < l+1:
                rows.append([])
            rows[l].append(c.val)
            if c.left:
                q.append((l+1, c.left))
            if c.right:
                q.append((l+1, c.right))
        result = []
        for i in rows:
            result.append(max(i))
        return result

