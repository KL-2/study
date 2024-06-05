"""LeetCode 第206题 反转链表

《剑指Offer第2版》第24题 反转链表"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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

class Solution(object):
    def trainningPlan_iterate(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre=None
        cur=head
        while(cur):
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
            
        return pre
    def trainningPlan_recursion(self,head):
        def recur(cur,pre):#递归返回翻转后的头结点
            if not cur:return pre#如果到cur不存在了，返回翻转后的头结点就是尾结点就是pre
            res=recur(cur.next,cur)#递归
            cur.next=pre#反向链接
            return res
        return recur(head,None)

if __name__=="__main__":
    list = [2,6,7,8,9]
    solution=Solution()
    head1=list_to_linkedlist(list)
    head2=list_to_linkedlist(list)
    print(solution.trainningPlan_iterate(head1).val)
    print(solution.trainningPlan_recursion(head2).val)