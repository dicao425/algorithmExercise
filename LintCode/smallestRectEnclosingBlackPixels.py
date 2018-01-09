#!/usr/bin/python
import sys


class Solution:
    """
    @param: image: a binary matrix with '0' and '1'
    @param: x: the location of one of the black pixels
    @param: y: the location of one of the black pixels
    @return: an integer
    """

    def minArea(self, image, x, y):
        # write your code here
        if not image or not image[0]:
            return 0
        # find left
        first = 0
        last = y
        while first + 1 < last:
            m = (first + last) / 2
            if self.checkCol(image, m):
                last = m
            else:
                first = m
        if self.checkCol(image, first):
            left = first
        else:
            left = last
        # find right
        first = y
        last = len(image[0]) - 1
        while first + 1 < last:
            m = (first + last) / 2
            if self.checkCol(image, m):
                first = m
            else:
                last = m
        if self.checkCol(image, last):
            right = last
        else:
            right = first
        # find top
        first = 0
        last = x
        while first + 1 < last:
            m = (first + last) / 2
            if self.checkRow(image, m):
                last = m
            else:
                first = m
        if self.checkRow(image, first):
            top = first
        else:
            top = last
        # find bottom
        first = x
        last = len(image) - 1
        while first + 1 < last:
            m = (first + last) / 2
            if self.checkRow(image, m):
                first = m
            else:
                last = m
        if self.checkRow(image, last):
            bottom = last
        else:
            bottom = first
        print bottom
        print top
        print right
        print left
        return (bottom - top + 1) * (right - left + 1)

    def checkCol(self, image, mid):
        for i in range(len(image)):
            if image[i][mid] == "1":
                return True
        return False

    def checkRow(self, image, mid):
        for i in range(len(image[0])):
            if image[mid][i] == "1":
                return True
        return False

def main():
    aa = Solution()
    print aa.minArea(["0010", "0110", "0100"], 0, 2)
    return 0

if __name__ == "__main__":
    sys.exit(main())