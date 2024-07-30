'''
LeetCode 第138题 复制带随机指针的链表

《剑指Offer第2版》 第35题 复杂链表的复制

给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val:一个表示 Node.val 的整数。
random_index:随机指针指向的节点索引（范围从 0 到 n-1);如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。
'''


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:return
        dic={}
        cur=head
        while cur:
            dic[cur]=Node(cur.val)
            #每一个cur对应一个值val，对应一个next的地址，对应一个random的地址
            # print(dic[cur].val)#给的值
            # print(dic[cur])#给的地址
            cur=cur.next
        cur=head
        print("cur.next的值")
        while cur:
            print(dic[cur].val)
            cur=cur.next
        cur=head
        print("cur.random的值")
        while cur:
            print(dic[cur.random].val)
            cur=cur.next
        cur=head
        while cur:
            dic[cur].next=dic.get(cur.next)#得到的是地址
            dic[cur].random=dic.get(cur.random)
            cur=cur.next
        
        return dic[head]
    
# Function to print the list for testing purposes
def print_list(head):
    nodes = []
    while head:
        random_val = head.random.val if head.random else None
        nodes.append(f"({head.val}, {random_val})")
        head = head.next
    return " -> ".join(nodes)

# Function to create the linked list from the given head input
def create_linked_list(data):
    if not data:
        return None
    
    # Create all nodes
    nodes = [Node(val[0]) for val in data]
    
    # Assign next and random pointers
    for i, val in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if val[1] is not None:
            nodes[i].random = nodes[val[1]]
    
    return nodes[0]

# Test code
if __name__ == "__main__":
    head_data = [[7,None],[13,0],[11,4],[10,2],[1,0],[3,None]]
    head = create_linked_list(head_data)

    solution = Solution()
    copied_head = solution.copyRandomList(head)

    # Print the original and copied list
    print("Original list:")
    print(print_list(head))
    print("\nCopied list:")
    print(print_list(copied_head))
