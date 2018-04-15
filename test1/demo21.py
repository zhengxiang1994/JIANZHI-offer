# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            if pushV and pushV[0] != popV[0]:
                stack.append(pushV.pop(0))
            elif pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))






