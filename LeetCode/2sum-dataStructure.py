#!/usr/bin/python
import sys

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.d[number] = self.d.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for item in self.d.keys():
            if value - item in self.d and (value - item != item or (value - item == item and self.d[item] > 1)):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())