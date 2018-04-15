# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        count = 0
        i = 0
        while i < len(array):
            count += 1
            if array[i] % 2 == 0:
                even = array[i]
                array.remove(even)
                array.append(even)
            else:
                i += 1
            if count > len(array)-1:
                break
        return array


if __name__ == "__main__":
    s = Solution()
    print(s.reOrderArray([1, 2, 3, 4, 5, 6]))


