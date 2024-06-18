'''《剑指Offer第2版》第26题 树的子结构
LCR 143. 子结构判断

给定两棵二叉树 tree1 和 tree2,判断 tree2 是否以 tree1 的某个节点为根的子树具有相同的结构和节点值 。
注意，空树不会是以 tree1 的某个节点为根的子树具有相同的结构和节点值 


'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        def recur(A,B):
            if not B:
                return True
            if not A:
                return False
            if A.val!=B.val:
                return False
            return recur(A.left,B.left) and recur(A.right,B.right)
        if A is None or B is None:
            return False
        return recur(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)

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



if __name__=="__main__":
    tree1_arr = [3,6,7,1,8]
    tree2_arr = [6, 1]

    # Build trees from arrays
    tree1 = buildTreeFromArray(tree1_arr)
    tree2 = buildTreeFromArray(tree2_arr)

    solution = Solution()
    result = solution.isSubStructure(tree1, tree2)
    print(result)