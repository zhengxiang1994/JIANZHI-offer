# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 0:
            return 0
        x = 1   # 可换成其他数字 1~9
        total = 0
        for i in range(1, len(str(n))+1):
            high = int(n / 10**i)   # 高位数字
            cur = int(int(n / 10**(i-1)) % 10)  # 本位数字
            low = int(n % 10**(i-1))    # 低位数字
            if cur == x:
                total += high * 10**(i-1) + (low+1)
            elif cur > x:
                total += (high+1) * 10**(i-1)
            else:
                total += high * 10**(i-1)
        return total



if __name__ == "__main__":
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution(2593))