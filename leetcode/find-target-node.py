'''
《剑指Offer第2版》第54题 二叉搜索树的第k大节点

LCR 174. 寻找二叉搜索树中的目标节点

某公司组织架构以二叉搜索树形式记录，节点值为处于该职位的员工编号。请返回第 cnt 大的员工编号。

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTargetNode(self, root, cnt):
        """
        :type root: Optional[TreeNode]
        :type cnt: int
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 
            dfs(root.right)#逆序中序遍历
            self.cnt-=1
            if self.cnt==0:
                self.res=root.val

                return self.res
            dfs(root.left)
        self.cnt=cnt
        dfs(root)
        return self.res