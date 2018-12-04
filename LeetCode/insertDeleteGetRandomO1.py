#!/usr/bin/python
import sys

import random

import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = dict()
        self.d = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.h:
            return False
        else:
            self.d.append(val)
            self.h[val] = len(self.d) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.h:
            return False
        else:
            idx = self.h[val]
            value = self.d[-1]
            self.h[value] = idx
            self.d[idx] = value
            self.d.pop()
            del self.h[val]
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.d:
            return
        return random.choice(self.d)  # self.d[random.randint(0, len(self.d) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())