'''
101. 对称二叉树
给你一个二叉树的根节点 root,检查它是否轴对称。

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ismirror(left,right):
            if(left is None )and(right is None):
                return True
            if (left is None )or(right is None):
                return False
            if left.val!=right.val:
                return False

            return ismirror(left.left,right.right) and ismirror(left.right,right.left)
        return ismirror(root,root)