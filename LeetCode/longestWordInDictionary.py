#!/usr/bin/python
import sys


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = ""
        s = set(words)
        for word in words:
            if len(word) > len(result) or len(word) == len(result) and word < result:
                if all([word[:k] in s for k in range(1, len(word))]):
                    result = word
        return result


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())