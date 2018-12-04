#!/usr/bin/python
import sys

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        result = [0] * n
        pre_time = 0
        for l in logs:
            fid, op, tm = l.split(":")
            tm = int(tm)
            fid = int(fid)
            if op == "start":
                if stack:
                    result[stack[-1]] += tm - pre_time
                stack.append(fid)
                pre_time = tm
            else:
                result[stack.pop()] += tm - pre_time + 1
                pre_time = tm + 1
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())