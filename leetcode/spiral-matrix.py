'''LeetCode 第54题 螺旋矩阵

《剑指Offer第2版》第29题 顺时针打印矩阵

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left=0
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1
        res=[]
        while True:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            if top>bottom:
                break
            
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            if left>right:
                break
            
            for i in range(right,left-1,-1):#注意这里是-1，不包含这个
                res.append(matrix[bottom][i])
            bottom-=1
            if top>bottom:
                break

            for i in range(bottom,top-1,-1):#注意这里是-1，不包含这个
                res.append(matrix[i][left])
            left+=1
            if left>right:
                break
        return res