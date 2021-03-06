#!/usr/bin/python
import sys

def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)

def merge(left, right):
    r = 0
    l = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result += left[l:]
    return result

# T Best- O(nlogn)  Ave - O(nlogn)  Worse - O(nlogn)    Space - O(n)

def main():
    print merge_sort([4,3,5,7,9,1,2,8])
    return 0

if __name__ == "__main__":
    sys.exit(main())
