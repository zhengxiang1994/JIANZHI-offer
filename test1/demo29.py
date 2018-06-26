# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        return sorted(tinput)[: k]


if __name__ == "__main__":
    s = Solution()
    print(s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))
