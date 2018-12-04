#!/usr/bin/python
import sys


class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        # if the comment starts with // we just substringfy everything and attach that to a list
        # if the comment starts with /* we need to add the string until the end

        return_list = []
        block_on = False
        cur_string = ""
        for source_string in source:
            index = 0
            while index < len(source_string):
                if block_on:
                    if source_string[index] == "*":
                        if index < len(source_string) - 1 and source_string[index + 1] == "/":
                            block_on = False
                            index += 1
                    else:
                        pass

                elif source_string[index] == "/":
                    if index < (len(source_string) - 1) and source_string[index + 1] == "*":
                        block_on = True
                        index += 1
                    elif index < (len(source_string) - 1) and source_string[index + 1] == "/":
                        break
                    else:
                        cur_string += source_string[index]
                else:
                    cur_string += source_string[index]
                index += 1
            if cur_string != "" and block_on == False:
                return_list.append(cur_string)
                cur_string = ""
        return return_list

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())