# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) == 0:
            return False
        root = sequence[-1]
        flag = 0
        while sequence[flag] < root:
            flag += 1
        for i in range(flag, len(sequence)-1):
            if sequence[i] < root:
                return False
        left = True
        right = True
        if flag > 0:
            left = self.VerifySquenceOfBST(sequence[:flag])
        if flag < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[flag:len(sequence)-1])
        return left and right


if __name__ == "__main__":
    s = Solution()
    print(s.VerifySquenceOfBST([1, 4, 7, 6, 3, 13, 14, 10, 8]))


