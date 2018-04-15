# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        ls = []
        p = head
        while p:
            ls.append(p.val)
            p = p.next
        if k > len(ls) or k == 0:
            return None
        else:
            return ls[len(ls)-k]


if __name__ == "__main__":
    s = Solution()
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln1.next = ln2
    ln2.next = ln3
    print(s.FindKthToTail(ln1, 3))



