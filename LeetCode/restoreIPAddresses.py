#!/usr/bin/python
import sys


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.dfs([], '', s)
        return self.result

    def dfs(self, curr_list, curr, rest):
        if curr and len(curr) > 1 and curr.startswith('0'):
            return
        if curr and int(curr) < 256:
            if len(curr_list) < 4:
                curr_list.append(curr)
                if len(curr_list) == 4:
                    if not rest:
                        self.result.append('.'.join(curr_list))
                    curr_list.pop()
                    return
        elif curr and int(curr) >= 256:
            return
        l = 0
        for i in range(len(rest)):
            l += 1
            if l > 3:
                break
            self.dfs(curr_list, rest[:i + 1], rest[i + 1:])
        if curr_list:
            curr_list.pop()
        return



def main():
    aa = Solution()
    print aa.restoreIpAddresses("25525511135")
    print aa.restoreIpAddresses("010010")
    return 0

if __name__ == "__main__":
    sys.exit(main())
