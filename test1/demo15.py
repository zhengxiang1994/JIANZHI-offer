# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        else:
            p1 = pHead
            p2 = pHead.next
            p1.next = None
            while p2:
                temp = p2.next
                p2.next = p1
                p1 = p2
                p2 = temp
            return p1


if __name__ == "__main__":
    s = Solution()
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln1.next = ln2
    ln2.next = ln3
    print(s.ReverseList(ln1))


