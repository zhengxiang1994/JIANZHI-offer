# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        # 类似冒泡排序
        for i in range(len(numbers)-1):
            for j in range(len(numbers)-i-1):
                if int(str(numbers[j])+str(numbers[j+1])) > int(str(numbers[j+1])+str(numbers[j])):
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        s = ""
        return s.join(list(map(str, numbers)))
            

if __name__ == "__main__":
    s = Solution()
    arr = [3, 32, 321]
    print(s.PrintMinNumber(arr))