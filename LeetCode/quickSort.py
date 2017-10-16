#!/usr/bin/python
import sys

def quick_sort(l, low, high):
    i = low
    j = high
    if i >= j:
        return l
    k = l[i]
    while i < j:
        while i < j and l[j] >= k:
            j -= 1
        l[i] = l[j]
        while i < j and l[i] <= k:
            i += 1
        l[j] = l[i]
    l[i] = k
    quick_sort(l, low, i-1)
    quick_sort(l, j+1, high)
    return l

# time comp   Best - O(nlogn)   Ave - O(nlogn)  Worse - O(n^2)  Space worse O(logn)

def main():
    print quick_sort([5,4,7,6,9,2,3,1], 0, 7)
    return 0

if __name__ == "__main__":
    sys.exit(main())
