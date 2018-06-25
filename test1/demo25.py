# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReConnectNodes(pHead)
    
    # 复制原始链表的任一节点N并创建新节点N',再把N'放在N的后面
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next
    
    # 如果原始链表上的节点N的random指向S,则对应的复制节点N'的random指向S'(S的下一个节点)
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next
    
    # 把得到的链表拆成两个链表，奇数位置上的节点组成原链表，偶数位置上的节点组成复制链表
    def ReConnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pHead.next
        while pNode:
            cloneNode = pNode.next
            pNode.next = cloneNode.next
            cloneNode.next = None if cloneNode.next is None else cloneNode.next.next
            pNode = pNode.next
        return pClonedHead


if __name__ == "__main__":
    p1 = RandomListNode(1)
    p2 = RandomListNode(2)
    p3 = RandomListNode(3)
    p4 = RandomListNode(4)
    p5 = RandomListNode(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p1.random = p3
    p2.random = p5
    p4.random = p2

    s = Solution()
    pClone = s.Clone(p1)
    pNode = pClone
    while pNode:
        print(pNode.label)
        pNode = pNode.next

