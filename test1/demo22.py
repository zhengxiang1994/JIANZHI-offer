# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        ls = []
        queue = []
        if not root:
            return ls
        queue.append(root)
        while queue:
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            ls.append(temp.val)
        return ls


if __name__ == "__main__":
    root0 = TreeNode(8)
    root1 = TreeNode(6)
    root2 = TreeNode(10)
    root3 = TreeNode(5)
    root4 = TreeNode(7)
    root5 = TreeNode(9)
    root6 = TreeNode(11)
    root0.left = root1
    root0.right = root2
    root1.left = root3
    root1.right = root4
    root2.left = root5
    root2.right = root6

    s = Solution()
    print(s.PrintFromTopToBottom(root0))


