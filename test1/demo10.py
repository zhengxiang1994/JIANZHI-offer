# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        n1 = 1
        n2 = 2
        n = 0
        if number == 1:
            return n1
        elif number == 2:
            return n2
        else:
            for i in range(number-2):
                n = n1 + n2
                n1 = n2
                n2 = n
        return n


if __name__ == "__main__":
    s = Solution()
    print(s.rectCover(4))
