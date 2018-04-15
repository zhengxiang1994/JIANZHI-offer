# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        time1 = 1
        time2 = 2
        times = 0
        if number == 1:
            times = 1
        elif number == 2:
            times = 2
        else:
            for i in range(number-2):
                times = time1 + time2
                time1 = time2
                time2 = times
        return times


if __name__ == "__main__":
    s = Solution()
    print(s.jumpFloor(4))


