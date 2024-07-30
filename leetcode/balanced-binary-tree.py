'''
剑指Offer第2版 55-2. 平衡二叉树
110. 平衡二叉树

给定一个二叉树，判断它是否是 
平衡二叉树

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recur(root):
            if not root:
                return 0
            left=recur(root.left)
            if left==-1:
                return -1
            right=recur(root.right)
            if right==-1:
                return -1
            if abs(right,left)<=-1:
                return max(left,right)+1
            else:
                return -1
        return recur(root)!=-1