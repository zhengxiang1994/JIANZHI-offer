# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        root = self.sub_reConstructBinaryTree(pre, 0, len(pre)-1, tin, 0, len(tin)-1)
        return root

    def sub_reConstructBinaryTree(self, pre, startPre, endPre, tin, startIn, endIn):
        if startPre > endPre or startIn > endIn:
            return None
        root = TreeNode(pre[startPre])

        for i in range(startIn, endIn+1):
            if tin[i] == pre[startPre]:
                root.left = self.sub_reConstructBinaryTree(pre, startPre+1, startPre+i-startIn, tin, startIn, i-1)
                root.right = self.sub_reConstructBinaryTree(pre, i-startIn+startPre+1, endPre, tin, i+1, endIn)
                break
        return root


if __name__ == "__main__":
    s = Solution()
    root = s.reConstructBinaryTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    print(root.left.left.right.val)




