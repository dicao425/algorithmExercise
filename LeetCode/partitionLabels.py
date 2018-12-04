#!/usr/bin/python
import sys

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d = {c: i for i, c in enumerate(S)}
        j = 0
        result = []
        for i, c in enumerate(S):
            j = max(j, d[c])
            if i == j:
                if not result:
                    result.append(i + 1)
                else:
                    result.append(i - sum(result) + 1)
        return result
'''
abbccadde
i 0  j 5
  1    5
  2    5
  3    5
  4    5
  5    5   V  a partition

if 'f' there
abb(f)ccadde   -- the same
abb(f)ccadde(f)  -- Will be extended to the last f's index
i 0  j 5
  1    5
  2    5
  3    5 -> 10
  4    5 -> 10
  ...
'''
def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())