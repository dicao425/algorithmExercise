#!/usr/bin/python
import sys

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        import heapq
        h = {}
        for r in results:
            if r.id in h:
                heapq.heappush(h[r.id], r.score)
                if len(h[r.id]) > 5:
                    heapq.heappop(h[r.id])
            else:
                h[r.id] = [r.score]
        a = {}
        for k, v in h.items():
            a[k] = sum(v) / 5.0
        return a


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())