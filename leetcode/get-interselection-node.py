'''
52. 两个链表的第一个公共节点

LCR 171. 训练计划 V

某教练同时带教两位学员，分别以链表 l1、l2 记录了两套核心肌群训练计划，节点值为训练项目编号。两套计划仅有前半部分热身项目不同，后续正式训练项目相同。请设计一个程序找出并返回第一个正式训练项目编号。如果两个链表不存在相交节点，返回 null 。

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1,lenp1=headA,0
        p2,lenp2=headB,0
        while p1:
            p1=p1.next
            lenp1+=1
        while p2:
            p2=p2.next
            lenp2+=1

        if lenp1<lenp2:#交换，p1是长链
            headA,headB=headB,headA
            lenp1,lenp2=lenp2,lenp1
        for _ in range(lenp1-lenp2):
            headA=headA.next#往后移进行尾端对齐
        while headA and headB:
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None