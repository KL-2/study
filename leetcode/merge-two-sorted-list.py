'''LeetCode 第21题 合并两个有序链表

《剑指Offer第2版》第25题 合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val>list2.val:
            list2.next=self.mergeTwoLists(list1,list2.next)
            return list2
        else:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1

if __name__=="__main__":
    solution=Solution()
    l1 = [1,2,4]
    l2 = [1,3,4]
    list1=list_to_linkedlist(l1)
    list2=list_to_linkedlist(l2)

    print(linkedlist_to_list(solution.mergeTwoLists(list1,list2)))