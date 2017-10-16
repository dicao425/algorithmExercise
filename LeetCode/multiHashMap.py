#!/usr/bin/python
import sys

class MultiHashMap(object):
    def __init__(self):
        self.hm = {}
        self.values = {}

    def _add_value(self, value):
        if value not in self.values:
            self.values[value] = 1
        else:
            self.values[value] += 1

    def _rm_value(self, value):
        self.values[value] -= 1
        if self.values[value] == 0:
            self.values.pop(value)

    def put(self, key, value):
        if key in self.hm:
            if value in self.hm[key]:
                return
            else:
                self.hm[key].add(value)
                self._add_value(value)
        else:
            self.hm[key] = set([value])
            self._add_value(value)

    def delete(self, key, value):
        if key in self.hm:
            if value in self.hm[key]:
                self.hm[key].remove(value)
                self._rm_value(value)
            else:
                return
        else:
            return

    def get(self, key):
        if key in self.hm:
            return self.hm[key]
        else:
            return set()

    def contains(self, value):
        if value in self.values:
            return True
        else:
            return False

def main():
    aa = MultiHashMap()
    aa.put('a', 1)
    aa.put('a', 2)
    aa.put('a', 2)
    aa.put('a', 3)
    aa.put('b', 1)
    aa.put('c', 5)
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())