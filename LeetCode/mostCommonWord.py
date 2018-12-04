#!/usr/bin/python
import sys

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        result = ("", -1)
        d = dict()
        paragraph = paragraph.replace(",", " ").replace(".", " ").replace(";", " ").replace("'", " ").replace("!", " ").replace("?", " ").replace('"', " ")
        for w in paragraph.split(" "):
            word = w.lower().strip()
            if word and word not in banned:
                d[word] = d.get(word, 0) + 1
                if d[word] > result[1]:
                    result = (word, d[word])
        return result[0]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())