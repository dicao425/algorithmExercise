#!/usr/bin/python
import sys


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.lru = {}
        self.head = None
        self.tail = None
        self.cap = capacity
        self.size = 0

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key not in self.lru:
            return -1
        node = self.lru[key]
        self.rm(node)
        self.top(node)
        return node.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key not in self.lru:
            self.top(Node(key, value))
        else:
            node = self.lru[key]
            node.value = value
            self.rm(node)
            self.top(node)

    def rm(self, node):
        # remove a node
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.prev = None
        node.next = None
        self.lru.pop(node.key)
        self.size -= 1

    def top(self, node):
        # add a new node
        if self.size == self.cap:
            self.rm(self.tail)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.lru[node.key] = node
        self.size += 1


def main():
    aa = LRUCache()
    return 0

if __name__ == "__main__":
    sys.exit(main())