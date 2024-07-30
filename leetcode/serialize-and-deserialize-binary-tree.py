'''LeetCode 第279题 二叉树的序列化与反序列化

《剑指Offer第2版》第37题 序列化二叉树

297. 二叉树的序列化与反序列化

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue=collections.deque()
        queue.append(root)
        res=[]
        while queue:
            node=queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')#这里是res加的
        return "["+",".join(res)+"]"#将字符串res中的元素用,分隔开

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="[]":return
        queue=collections.deque()
        val=data[1:-1].split(",")
        i=1

        root=TreeNode(int(val[0]))
        queue.append(root)
        while queue:
            node=queue.popleft()
            if val[i]!='null':
                node.left=TreeNode(int(val[i]))
                queue.append(node.left)
            i+=1
            if val[i]!='null':
                node.right=TreeNode(int(val[i]))
                queue.append(node.right)
            i+=1
        return root




if __name__=="__main__":
    a=[2,3,4,5]
    print(a[1:-1])