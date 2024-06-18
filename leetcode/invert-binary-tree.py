'''226. 翻转二叉树

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
LeetCode 第226题 翻转二叉树

《剑指Offer第2版》第27题 二叉树的镜像

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTreeFromArray(arr):
    if not arr:
        return None
    
    def buildTreeHelper(index):
        if index >= len(arr) or arr[index] is None:
            return None
        
        node = TreeNode(arr[index])
        node.left = buildTreeHelper(2 * index + 1)
        node.right = buildTreeHelper(2 * index + 2)
        
        return node
    
    return buildTreeHelper(0)

def printTree(root):
    if not root:
        return
    
    queue = [root]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

class Solution:
    def invertbinarytree(self,root):
        if not root:
            return root#是指没有子结点
        left=self.invertbinarytree(root.left)
        right=self.invertbinarytree(root.right)
        root.left,root.right=right,left
        return root 

if __name__=="__main__":
    solution=Solution()
    root = [4,2,7,1,3,6,9]
    print(printTree(solution.invertbinarytree(buildTreeFromArray(root))))
