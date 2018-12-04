#!/usr/bin/python
import sys


class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.d:
            self.d[message] = timestamp
            return True
        else:
            if self.d[message] + 10 <= timestamp:
                self.d[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())