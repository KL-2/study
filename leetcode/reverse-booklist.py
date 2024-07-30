'''
LCR 123. 图书整理 I
剑指Offer第2版 6. 从尾到头打印链表
书店店员有一张链表形式的书单，每个节点代表一本书，节点中的值表示书的编号。为更方便整理书架，店员需要将书单倒过来排列，就可以从最后一本书开始整理，逐一将书放回到书架上。请倒序返回这个书单链表。


'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBookList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if head:
            return self.reverseBookList(head.next)+[head.val]
        else:
            return []