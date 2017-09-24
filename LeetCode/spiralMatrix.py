class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.result = []
        self.helper(matrix)
        return self.result

    def helper(self, m):
        if m:
            self.result += m.pop(0)
            self.helper(self.rotate(m))

    def rotate(self, m):
        return zip(*m)[::-1]

