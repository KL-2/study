'''

LeetCode 第240题 搜索二维矩阵 II Search a 2D Matrix II

《剑指Offer第2版》第68-2题 二维数组中的查找

LCR 121. 寻找目标值 - 二维数组

m*n 的二维数组 plants 记录了园林景观的植物排布情况，具有以下特性：

每行中，每棵植物的右侧相邻植物不矮于该植物；
每列中，每棵植物的下侧相邻植物不矮于该植物。
 
请判断 plants 中是否存在目标高度值 target。

todo:还没做的题

3.12 发散思维能力
LeetCode By Python: 剑指Offer第2版 64. 求1+2+…+n
LeetCode By Python: 剑指Offer第2版 65. 不用加减乘除做加法
LeetCode By Python: 剑指Offer第2版 66. 构建乘积数组
3.13 面试案例
LeetCode By Python: 剑指Offer第2版 67. 把字符串转换成整数
LeetCode By Python: 235. 剑指Offer第2版68-1. 二叉搜索树最近公共祖先
LeetCode By Python 236: 剑指Offer第2版 68-2. 二叉树最近公共祖先

'''

class Solution(object):
    def findTargetIn2DPlants(self, plants, target):
        """
        :type plants: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i,j=len(plants)-1,0
        while i>=0 and j<=len(plants[0])-1:
            if plants[i][j]>target:
                i-=1
            elif plants[i][j]<target:
                j+=1
            else:return True
        return False   
