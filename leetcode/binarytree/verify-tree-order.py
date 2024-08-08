'''《剑指Offer第2版》第33题 二叉搜索树的后序遍历序列

LCR 152. 验证二叉搜索树的后序遍历序列

请实现一个函数来判断整数数组 postorder 是否为二叉搜索树的后序遍历结果。


'''

class Solution(object):
    def verifyTreeOrder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if not postorder:
            return True
        root=postorder[-1] # 得到根节点
        # cur_index=0
        for i in range(len(postorder)):
            if postorder[i]>root: # 找到左子树终点
                # cur_index=i
                break
        left=postorder[:i]
        right=postorder[i:-1]
        for i in right:
            if i<root:
                return False
        return self.verifyTreeOrder(left) and self.verifyTreeOrder(right)#这里是left和right