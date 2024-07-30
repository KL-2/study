'''
LeetCode 第105题 从前序与中序遍历序列构造二叉树

《剑指Offer第2版》第7题 重建二叉树

LCR 124. 推理二叉树

某二叉树的先序遍历结果记录于整数数组 preorder，它的中序遍历结果记录于整数数组 inorder。请根据 preorder 和 inorder 的提示构造出这棵二叉树并返回其根节点。

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def deduceTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder)==0:
            return None
        root=TreeNode(preorder[0])
        # Root index in inorder
        # Python List has built-in .index() function to return value index
        index=inorder.index(preorder[0])
        root.left=self.deduceTree(preorder[1:index+1],inorder[:index])
        root.right=self.deduceTree(preorder[index+1:],inorder[index+1:])
        return root
