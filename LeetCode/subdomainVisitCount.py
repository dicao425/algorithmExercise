#!/usr/bin/python
import sys

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = dict()
        result = []
        for s in cpdomains:
            n, domain = s.split()
            while domain:
                d[domain] = d.get(domain, 0) + int(n)
                i = domain.find('.')
                if i == -1:
                    break
                else:
                    domain = domain[i+1:]
        for k, v in d.items():
            result.append(' '.join([str(v), k]))
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())