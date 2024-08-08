'''
LeetCode 第426题 将二叉搜索树转化为排序的双向链表

《剑指Offer第2版》第36题 二叉搜索树与双向链表
LCR 155. 将二叉搜索树转化为排序的双向链表

将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。

对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:return
        def dfs(cur):
            if not cur:return
            dfs(cur.left)#中序遍历
            # 此时左子树已经排好序而且双向了
            if not self.pre:
                self.head=cur#设置head作为起点
            else:
                cur.left=self.pre#双向，和左子树最大的链接
                self.pre.right=cur#左子树最大的和cur链接
            self.pre=cur
            dfs(cur.right)
        self.pre=None
        dfs(root)
        self.head.left=self.pre#循环
        self.pre.right=self.head
        return self.head