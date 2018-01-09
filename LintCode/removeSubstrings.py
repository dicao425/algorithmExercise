#!/usr/bin/python
import sys

class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        if not s:
            return 0
        result = len(s)
        h = {s}
        q = [s]
        while q:
            cur = q.pop(0)
            for k in dict:
                idx = cur.find(k)
                while idx != -1:
                    new_s = cur[:idx] + cur[idx+len(k):]
                    if new_s not in h:
                        result = min(result, len(new_s))
                        h.add(new_s)
                        q.append(new_s)
                    idx = cur.find(k, idx+1)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())