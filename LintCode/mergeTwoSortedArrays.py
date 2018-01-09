#!/usr/bin/python
import sys

class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        result = []
        i = 0
        j = 0
        while i <= len(A)-1 and j <= len(B)-1:
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        if i <= len(A) -1:
            result.extend(A[i:])
        if j <= len(B) - 1:
            result.extend(B[j:])
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())