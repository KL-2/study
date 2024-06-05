'''LCR 136. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
《剑指Offer第2版》第18题 删除链表的节点
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val==val:
            return head.next
        pre,cur=head,head.next
        while cur and cur.val!=val:
            pre,cur=cur,cur.next
        if cur:
            pre.next=cur.next
        return head

def list_to_linkedlist(list):
    if not list:
        return None
    head = ListNode(list[0])
    current = head
    for value in list[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linkedlist_to_list(head):
    list = []
    current = head
    while current:
        list.append(current.val)
        current = current.next
    return list

if __name__=="__main__":
    solution=Solution()
    head_list=[1,3,4,5]
    val=6
    head = list_to_linkedlist(head_list)
    new_head = solution.deleteNode(head, val)
    print(linkedlist_to_list(new_head))
