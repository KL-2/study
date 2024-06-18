'''
LCR 149. 彩灯装饰记录 I
《剑指Offer第2版》第32-I题 从上到下打印二叉树
一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从 左 到 右 的顺序返回每一层彩灯编号。

'''


class Solution(object):
    def decorateRecord(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        res=[]
        queue=collections.deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
    
'''
LeetCode 第102题 二叉树的层次遍历

《剑指Offer第2版》第32-II题 从上到下打印二叉树 II
102. 二叉树的层序遍历

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        queue=collections.deque()
        queue.append(root)
        while queue:
            size=len(queue)
            tmp=[]
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)

        return res


'''
《剑指Offer第2版》第32-III题 从上到下打印二叉树 III
LCR 151. 彩灯装饰记录 III

一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照如下规则记录彩灯装饰结果：

第一层按照从左到右的顺序记录
除第一层外每一层的记录顺序均与上一层相反。即第一层为从左到右，第二层为从右到左。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def decorateRecord(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        queue=collections.deque()
        queue.append(root)
        while queue:
            tmp=[]
            for _ in range(len(queue)):
                node=queue.popleft()        
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(tmp)
            if not queue:
                break
            tmp=[]
            for _ in range(len(queue)):#这里要len(queue)重新计算
                node =queue.pop()#反向
                tmp.append(node.val)
                if node.right:
                    queue.appendleft(node.right)#反向顺序变换

                if node.left:
                    queue.appendleft(node.left)
            res.append(tmp)
        return res

















