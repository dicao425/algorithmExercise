#!/usr/bin/python
import sys

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for w in words:
            tmp = []
            for c in w:
                tmp.append(d[ord(c)-97])
            result.add(''.join(tmp))
        return len(result)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())