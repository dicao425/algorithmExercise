#!/usr/bin/python
import sys


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.dict_lru = {}
        self.head = None
        self.tail = None
        self.cap = capacity
        self.size = 0

    def get(self, key):
        if key not in self.dict_lru:
            return -1
        node = self.dict_lru[key]
        self.rm(node)
        self.top(node)
        return node.value

    def set(self, key, value):
        if key not in self.dict_lru:
            self.top(Node(key, value))
        else:
            node = self.dict_lru[key]
            node.value = value
            self.rm(node)
            self.top(node)

    def rm(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.dict_lru.pop(node.key)
        self.size -= 1

    def top(self, node):
        if self.size == self.cap:
            self.rm(self.tail)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.dict_lru[node.key] = node
        self.size += 1


def main():
    aa = LRUCache()
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())