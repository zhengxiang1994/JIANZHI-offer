# -*- coding:utf-8 -*-
class Solution:
    def quicksort(self, L, left, right):
        i = left
        j = right
        if i >= j:
            return L
        key = L[i]
        while i < j:
            while i < j and L[j] >= key:
                j -= 1
            while i < j and L[i] <= key:
                i += 1
            if i < j:
                L[i], L[j] = L[j], L[i]
        L[left] = L[i]
        L[i] = key

        self.quicksort(L, left, i-1)
        self.quicksort(L, j+1, right)


if __name__ == "__main__":
    s = Solution()
    ls = [1, 3, 5, 7, 2, 4, 6]
    s.quicksort(ls, 0, 6)
    print(ls)

