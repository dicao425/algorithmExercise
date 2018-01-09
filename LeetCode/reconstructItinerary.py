#!/usr/bin/python
import sys


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.targets = {}
        for a, b in sorted(tickets)[::-1]:
            self.targets[a] = self.targets.get(a, []) + [b]
        self.result = []
        self.dfs('JFK')
        return self.result[::-1]

    def dfs(self, ap):
        while ap in self.targets and self.targets[ap]:
            self.dfs(self.targets[ap].pop())
        self.result.append(ap)

def main():
    aa = Solution()
    print aa.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    print aa.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
    print aa.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
    return 0

if __name__ == "__main__":
    sys.exit(main())