#!/usr/bin/python
import sys


class LogSystem1(object):
    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.logs.append((timestamp, id))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        s_num = self.convert(s, gra)
        e_num = self.convert(e, gra)
        result = []
        for t in self.logs:
            if s_num <= self.convert(t[0], gra) <= e_num:
                result.append(t[1])
        return result

    def convert(self, str_time, gra):
        YY, MM, DD, hh, mm, ss = str_time.split(':')
        num = 0
        num += (int(YY) - 1999) * 12 * 31 * 24 * 60 * 60
        if gra == 'Year':
            return num
        num += int(MM) * 31 * 24 * 60 * 60
        if gra == 'Month':
            return num
        num += int(DD) * 24 * 60 * 60
        if gra == 'Day':
            return num
        num += int(hh) * 60 * 60
        if gra == 'Hour':
            return num
        num += int(mm) * 60
        if gra == 'Minute':
            return num
        num += int(ss)
        return num


class LogSystem:
    def __init__(self):
        self.times = []
        self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id, timestamp):
        self.times.append([timestamp, id])

    def retrieve(self, s, e, gra):
        ind = self.g[gra]
        s, e = s[:ind], e[:ind]
        return [i for time, i in self.times if s <= time[:ind] <= e]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())