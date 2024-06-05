'''LCR 022. 环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1,则在该链表中没有环。注意,pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_linkedlist(lst, pos):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    cycle_entry = None
    if pos == 0:
        cycle_entry = head
    for index, value in enumerate(lst[1:], 1):
        current.next = ListNode(value)
        current = current.next
        if index == pos:
            cycle_entry = current
    #到结尾了
    if cycle_entry is not None:  # Create the cycle if pos is not -1
        current.next = cycle_entry
    return head

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast,slow=head,head

        while True:
            if not (fast and fast.next): return
            #这里的解释：1.fast要在fast.next前，否则输入是[]时会报错
            #2.return这样意思是return None

            fast,slow=fast.next.next,slow.next
            if fast==slow:#快慢指针，直至slow进到环里
                break
        fast=head#开始记录head到环起点的距离
        while fast!=slow:
            fast,slow=fast.next,slow.next
        return fast
    
if __name__=="__main__":
    solution=Solution()

    head = [3, 2, 0, -4]
    pos = 1
    linkedlist = list_to_linkedlist(head, pos)
    result_node = solution.detectCycle(linkedlist)
    result_val = result_node.val if result_node else None
    print(f"Test case 1 - Expected: 2, Got: {result_val}")