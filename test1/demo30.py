# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = array[0]
        cur = array[0]
        for i in range(1, len(array)):
            cur = max(cur+array[i], array[i])   # 如果cur+array[i]<array[i]的话，那么之前子向量的头肯定不是所求子向量的头，因为array[i]更大
            res = max(cur, res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))


