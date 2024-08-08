'''LeetCode 第113题 路径总和 II

《剑指Offer第2版》 第34题 二叉树中和为某一值的路径

113. 路径总和 II  

给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        path=[]
        res=[]
        def recur(root,tar):
            if not root:
                return
            path.append(root.val)
            tar-=root.val
            if tar==0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left,tar)
            recur(root.right,tar)
            path.pop()# path 弹出了root.val

        recur(root,targetSum)
        return res

