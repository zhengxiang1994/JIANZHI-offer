# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2:
            return False
        if not pRoot1 and pRoot2:
            return False
        flag = False
        if pRoot1.val == pRoot2.val:
            flag = self.isSubtree(pRoot1, pRoot2)
        if not flag:
            flag = self.HasSubtree(pRoot1.left, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.right, pRoot2)
        return flag

    def isSubtree(self, root1, root2):
        if not root2:
            return True
        if not root1 and root2:
            return False
        if root1.val == root2.val:
            return self.isSubtree(root1.left, root2.left) and self.isSubtree(root1.right, root2.right)
        return False


if __name__ == "__main__":
    s = Solution()
    root10 = TreeNode(8)
    root11 = TreeNode(9)
    root12 = TreeNode(2)
    root13 = TreeNode(1)
    root14 = TreeNode(3)
    root15 = TreeNode(4)
    root10.left = root11
    root10.right = root12
    root11.left = root13
    root11.right = root14
    root12.left = root15

    root20 = TreeNode(9)
    root21 = TreeNode(1)
    root22 = TreeNode(3)
    root20.left = root21
    root20.right = root22

    print(s.HasSubtree(root10, root20))




