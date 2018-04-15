
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        else:
            return 2 * self.jumpFloorII(number-1)


if __name__ == "__main__":
    s = Solution()
    print(s.jumpFloorII(4))
