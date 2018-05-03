# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []
        self.temp = []

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return self.result
        self.temp.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and root.left is None and root.right is None:
            self.result.append(self.temp[:])    # python2.x deep copy
        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        self.temp.pop(-1)
        return self.result


if __name__ == "__main__":
    s = Solution()
    node0 = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(3)
    node6 = TreeNode(6)
    node0.left = node1
    node0.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    print(s.FindPath(node0, 7))




