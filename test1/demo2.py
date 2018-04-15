# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(" ", "%20")


if __name__ == "__main__":
    s = Solution()
    print(s.replaceSpace("We Are Happy"))

