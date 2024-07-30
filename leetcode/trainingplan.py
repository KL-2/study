'''
LeetCode 第206题 反转链表

《剑指Offer第2版》第24题 反转链表
LCR 141. 训练计划 III

给定一个头节点为 head 的单链表用于记录一系列核心肌群训练编号，请将该系列训练编号 倒序 记录于链表并返回。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def trainningPlan(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def recur(cur,pre):
            if not cur:return pre
            res=recur(cur.next,cur)
            cur.next=pre
            return res
        return recur(head,None)