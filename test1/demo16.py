# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        p1 = pHead1
        p2 = pHead2
        pHead = None
        temp = None
        while p1 and p2:
            if p1.val <= p2.val:
                if pHead is None:
                    pHead = p1
                    temp = pHead
                    p1 = p1.next
                else:
                    temp.next = p1
                    temp = temp.next
                    p1 = p1.next
            else:
                if pHead is None:
                    pHead = p2
                    temp = pHead
                    p2 = p2.next
                else:
                    temp.next = p2
                    temp = temp.next
                    p2 = p2.next
        if p1:
            temp.next = p1
        else:
            temp.next = p2
        return pHead


if __name__ == "__main__":
    s = Solution()
    ln1 = ListNode(1)
    ln2 = ListNode(3)
    ln3 = ListNode(5)
    ln1.next = ln2
    ln2.next = ln3

    ln4 = ListNode(2)
    ln5 = ListNode(4)
    ln6 = ListNode(6)
    ln4.next = ln5
    ln5.next = ln6

    ln = s.Merge(ln1, ln4)
    p = ln
    while p:
        print(p.val)
        p = p.next

