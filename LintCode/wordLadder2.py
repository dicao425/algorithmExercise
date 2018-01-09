#!/usr/bin/python
import sys

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        self.result = []
        self.d = dict
        self.distance = {}
        self.map = {}
        self.d.add(start)
        self.d.add(end)
        self.bfs(end)
        self.dfsf(start, end, [])
        return self.result

    def dfsf(self, current_word, end, path):
        if current_word == end:
            self.result.append(path + [end])
            return

        for next_word in self.map.get(current_word, []):
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


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())