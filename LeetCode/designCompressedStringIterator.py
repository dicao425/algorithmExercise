#!/usr/bin/python
import sys


class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.s = compressedString
        self.p = 0
        self.num = 0
        self.ch = ''

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        if self.num == 0:
            self.ch = self.s[self.p]
            self.p += 1
            while self.p < len(self.s) and not self.s[self.p].isalpha():
                self.num = self.num * 10 + int(self.s[self.p])
                self.p += 1
        self.num -= 1
        return self.ch

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.s) == self.p and self.num == 0:
            return False
        return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

def main():
    aa = StringIterator()
    return 0

if __name__ == "__main__":
    sys.exit(main())