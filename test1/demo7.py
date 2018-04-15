# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        fib1 = 1
        fib2 = 1
        if n == 1 or n == 2:
            return 1
        else:
            fib = 0
            for i in range(n-2):
                fib = fib1 + fib2
                fib1 = fib2
                fib2 = fib
            return fib


if __name__ == "__main__":
    s = Solution()
    print(s.Fibonacci(6))


