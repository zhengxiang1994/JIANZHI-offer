# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        coloums = len(array[0])
        i = rows - 1
        j = 0
        while i >= 0 and j < coloums:
            if target > array[i][j]:
                j += 1
            elif target < array[i][j]:
                i -= 1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.Find(6, [[1, 2, 5], [3, 4, 6], [7, 8, 9]]))






