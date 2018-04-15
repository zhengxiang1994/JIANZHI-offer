# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ls = []
        p = listNode
        while p:
            ls.append(p.val)
            p = p.next
        ls.reverse()
        return ls


if __name__ == "__main__":
    ln1 = ListNode(1)
    ln2 = ln1.next = ListNode(2)
    ln3 = ln2.next = ListNode(3)
    s = Solution()
    print(s.printListFromTailToHead(ln1))
