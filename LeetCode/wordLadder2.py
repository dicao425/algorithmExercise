#!/usr/bin/python
import sys
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.results = []
        self.end = endWord
        self.s = set(wordList)
        self.map = {}
        for
        self.dfs(self.s, beginWord, [beginWord])
        l = float('inf')
        for i in self.results:
            l = min(l, len(i))
        return [i for i in self.results if len(i) == l]

    def dfs(self, d, curr, result):
        if curr == self.end:
            self.results.append(result[:])
            return
        for i in range(len(curr)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new = curr[:i] + c + curr[i+1:]
                if new in d:
                    result.append(new)
                    d.remove(new)
                    self.dfs(d, new, result)
                    d.add(new)
                    result.pop()
        return

    def ladderLength1(self, beginWord, endWord, wordList):
        # DFS
        stack = []
        s = set(wordList)
        stack.append([beginWord])
        result = []
        l = float('inf')
        while stack:
            items = stack.pop()
            print items
            if len(items) > l:
                continue
            w = items[-1]
            for i in range(len(w)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new = w[:i] + c + w[i+1:]
                    if new == endWord:
                        l = min(l, len(items)+1)
                        result.append(items+[new])
                        break
                    if new in s:
                        stack.append(items+[new])
            import pdb
            pdb.set_trace()
        return result



def main():
    '''
    beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
    :return:
    '''
    aa = Solution()
    print aa.ladderLength1("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    cc="qa"
    bb="sq"
    dd=["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    print aa.ladderLength1(cc,bb,dd)
    return 0

if __name__ == "__main__":
    sys.exit(main())
'''
"qa"
"sq"
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
'''