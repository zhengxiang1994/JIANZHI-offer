# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        num = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if numbers[i] == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                num = numbers[i]
                count = 1

        count = 0
        for i in range(len(numbers)):
            if num == numbers[i]:
                count += 1
        if count * 2 > len(numbers):
            return num
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    print(s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))


