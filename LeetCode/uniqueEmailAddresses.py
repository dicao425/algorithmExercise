#!/usr/bin/python
import sys

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = set()
        for e in emails:
            local_name, domain = e.split('@')
            idx = local_name.find('+')
            if idx != -1:
                local_name = local_name[:idx]
            local_name = local_name.replace('.', '')
            s.add('@'.join([local_name, domain]))
        return len(s)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())