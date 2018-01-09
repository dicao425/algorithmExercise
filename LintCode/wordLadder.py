#!/usr/bin/python
import sys

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        q = [(start, 1)]
        if end not in dict:
            dict.add(end)
        step = 1
        while q:
            cur, step = q.pop(0)
            if cur == end:
                return step
            for i in range(len(cur)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_w = cur[:i] + c + cur[i+1:]
                    if new_w in dict:
                        q.append((new_w, step+1))
                        dict.remove(new_w)
        return step

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())