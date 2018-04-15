# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            if root.left:
                self.Mirror(root.left)
            if root.right:
                self.Mirror(root.right)

    def preOrderTraverse(self, root):
        if root:
            print(root.val)
            self.preOrderTraverse(root.left)
            self.preOrderTraverse(root.right)


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
    s.Mirror(root0)
    s.preOrderTraverse(root0)




