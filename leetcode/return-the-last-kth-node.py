'''《剑指Offer第2版》第 22 题 链表中倒数第k个节点

LCR 140. 训练计划 II

给定一个头节点为 head 的链表用于记录一系列核心肌群训练项目编号，请查找并返回倒数第 cnt 个训练项目编号。

'''
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



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def trainingPlan(self, head, cnt):
        """
        :type head: Optional[ListNode]
        :type cnt: int
        :rtype: Optional[ListNode]
        """
        former,latter=head,head
        for _ in range(cnt-1):
            former=former.next
        while(former.next):
            former,latter=former.next,latter.next
        return latter
    

if __name__=="__main__":
    solution=Solution()
    head_list=[2,4,7,8]
    cnt=1
    head = list_to_linkedlist(head_list)
    result = solution.trainingPlan(head,cnt)
    print(linkedlist_to_list(result))0