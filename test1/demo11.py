# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n).count("1") if n >= 0 else bin(2**32+n).count("1")


if __name__ == "__main__":
    s = Solution()
    print(s.NumberOf1(-5))


