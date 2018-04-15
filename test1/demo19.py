# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result += matrix[0]
            if not matrix or not matrix[0]:
                break
            matrix.pop(0)
            if matrix:
                matrix = self.rotate(matrix)
        return result

    def rotate(self, matrix):
        height = len(matrix)
        width = len(matrix[0])
        newmat = []
        for i in range(width):
            newmat.append([m[width-i-1] for m in matrix])
        return newmat


if __name__ == "__main__":
    s = Solution()
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(s.printMatrix(a))



