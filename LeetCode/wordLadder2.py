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
        # BFS
        q = []
        s = set(wordList)
        q.append([beginWord])
        result = []
        l = float('inf')
        while q:
            items = q.pop(0)
            # print items
            if len(items) > l:
                continue
            w = items[-1]
            for i in range(len(w)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new = w[:i] + c + w[i+1:]
                    if new == endWord:
                        cur_l = len(items)+1
                        if cur_l < l:
                            result = [items+[new]]
                            l = cur_l
                        else:
                            result.append(items+[new])
                        break
                    if new in s:
                        q.append(items+[new])
        return result

    # Lintcode
    def findLadder(self, start, end, dictionary):
        self.result = []
        self.d = dictionary
        self.distance = {}
        self.map = {}
        self.d += [start]
        self.bfs(end)
        self.dfsf(start, end, [])
        return self.result

    def dfsf(self, current_word, end, path):
        if current_word == end:
            self.result.append(path + [end])
            return

        for next_word in self.map[current_word]:
            if self.distance[current_word] == self.distance[next_word] + 1:
                path.append(current_word)
                self.dfsf(next_word, end, path)
                path.pop()

    def bfs(self, end):
        q = [end]
        visited = {end}
        dis = 0
        while q:
            for _ in range(len(q)):
                word = q.pop(0)
                self.distance[word] = dis
                next_words = self.get_next(word)
                self.map[word] = next_words
                for next_word in next_words:
                    if next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)
            dis += 1

    def get_next(self, word):
        next_words = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new = word[:i] + c + word[i+1:]
                if new != word and new in self.d:
                    next_words.append(new)
        return next_words


class Solution_Leetcode(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.result = []
        self.d = wordList
        self.distance = {}
        self.map = {}
        self.d += [beginWord]
        self.bfs(endWord)
        self.dfs(beginWord, endWord, [])
        return self.result

    def dfs(self, current_word, end, path):
        if current_word == end:
            self.result.append(path + [end])
            return

        for next_word in self.map.get(current_word, []):
            if self.distance[current_word] == self.distance[next_word] + 1:
                path.append(current_word)
                self.dfs(next_word, end, path)
                path.pop()

    def bfs(self, end):
        q = [end]
        visited = {end}
        dis = 0
        while q:
            for _ in range(len(q)):
                word = q.pop(0)
                self.distance[word] = dis
                next_words = self.get_next(word)
                self.map[word] = next_words
                for next_word in next_words:
                    if next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)
            dis += 1

    def get_next(self, word):
        next_words = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new = word[:i] + c + word[i + 1:]
                if new != word and new in self.d:
                    next_words.append(new)
        return next_words


def main():
    '''
    beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
    :return:
    '''
    aa = Solution_Leetcode()
    print aa.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    cc="qa"
    bb="sq"
    dd=["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    print aa.findLadders(cc,bb,dd)

    return 0

if __name__ == "__main__":
    sys.exit(main())
'''
"qa"
"sq"
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
'''