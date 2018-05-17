# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0

    def permu(self, arr, len, index):
        if index == len:
            self.sum += 1
            print(arr)
        else:
            for i in range(index, len):
                self.swap(arr, index, i)
                self.permu(arr, len, index+1)
                self.swap(arr, index, i)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr1 = [1, 2, 3]
    s = Solution()
    s.permu(arr1, 3, 0)

