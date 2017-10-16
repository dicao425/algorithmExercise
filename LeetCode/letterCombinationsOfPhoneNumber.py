#!/usr/bin/python
import sys

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "}
        result = [''] if digits else []
        for i in digits:
            result = [b+a for a in d[i] for b in result]
        return result

def main():
    aa = Solution()
    print aa.letterCombinations()
    return 0

if __name__ == "__main__":
    sys.exit(main())
