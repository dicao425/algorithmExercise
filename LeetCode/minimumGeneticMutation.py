#!/usr/bin/python
import sys


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # BFS
        q = [(start, 0)]
        hset = set(bank)
        while q:
            s, step = q.pop(0)
            if s == end:
                return step
            for i in range(len(start)):
                for ch in "ACGT":
                    new_string = s[:i] + ch + s[i + 1:]
                    if new_string in hset:
                        q.append((new_string, step + 1))
                        hset.remove(new_string)
        return -1


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())