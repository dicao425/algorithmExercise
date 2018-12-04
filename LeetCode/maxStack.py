#!/usr/bin/python
import sys

import heapq


class MaxStack(object):
    def __init__(self):
        """ Space  O N
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """ O 1
        :type x: int
        :rtype: void
        """
        m = max(self.stack[-1][1] if self.stack else -float('inf'), x)
        self.stack.append((x, m))

    def pop(self):
        """ O 1
        :rtype: int
        """
        return self.stack.pop()[0]

    def top(self):
        """ O 1
        :rtype: int
        """
        return self.stack[-1][0]

    def peekMax(self):
        """ O 1
        :rtype: int
        """
        return self.stack[-1][1]

    def popMax(self):
        """ O N
        :rtype: int
        """
        tmp = []
        m = self.stack[-1][1]
        while self.stack[-1][0] != m:
            tmp.append(self.pop())
        self.pop()
        map(self.push, reversed(tmp))
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

class MaxStack1(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxHeap = []
        self.toPop_heap = {}  # to keep track of things to remove from the heap
        self.toPop_stack = set()  # to keep track of things to remove from the stack

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        heapq.heappush(self.maxHeap, (-x, -len(self.stack)))
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.top()
        x = self.stack.pop()
        key = (-x, -len(self.stack))
        self.toPop_heap[key] = self.toPop_heap.get(key, 0) + 1
        return x

    def top(self):
        """
        :rtype: int
        """
        while self.stack and len(self.stack) - 1 in self.toPop_stack:
            x = self.stack.pop()
            self.toPop_stack.remove(len(self.stack))
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        while self.maxHeap and self.toPop_heap.get(self.maxHeap[0], 0):
            x = heapq.heappop(self.maxHeap)
            self.toPop_heap[x] -= 1
        return -self.maxHeap[0][0]

    def popMax(self):
        """
        :rtype: int
        """
        self.peekMax()
        x, idx = heapq.heappop(self.maxHeap)
        x, idx = -x, -idx
        self.toPop_stack.add(idx)
        return x

class MaxStack2(list):
    def push(self, x):
        m = max(x, self[-1][1] if self else None)
        self.append((x, m))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0]

    def peekMax(self):
        return self[-1][1]

    def popMax(self):
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        map(self.push, reversed(b))
        return m

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())