#!/usr/bin/python
import sys


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' not in IP and ':' not in IP:
            return 'Neither'
        if '.' in IP and ':' not in IP:
            if IP.count('.') == 3:
                items = IP.split('.')
                for item in items:
                    try:
                        if int(item) < 0 or int(item) > 255 or str(int(item)) != item:
                            return 'Neither'
                    except:
                        return 'Neither'
                return 'IPv4'
            else:
                return 'Neither'
        if ':' in IP and '.' not in IP:
            if IP.count(':') == 7:
                items = IP.split(':')
                for item in items:
                    try:
                        if len(item) > 4 or int(item, 16) < 0 or item[0] == '-':
                            return 'Neither'
                    except:
                        return 'Neither'
                return 'IPv6'
            else:
                return 'Neither'

        return 'Neither'


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())