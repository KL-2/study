'''
剑指Offer 47. 礼物的最大价值

LCR 166. 珠宝的最高价值

现有一个记作二维矩阵 frame 的珠宝架，其中 frame[i][j] 为该位置珠宝的价值。拿取珠宝的规则为：

只能从架子的左上角开始拿珠宝
每次可以移动到右侧或下侧的相邻位置
到达珠宝架子的右下角时，停止拿取
注意：珠宝的价值都是大于 0 的。除非这个架子上没有任何珠宝，比如 frame = [[0]]。

'''

class Solution(object):
    def jewelleryValue(self, frame):
        """
        :type frame: List[List[int]]
        :rtype: int
        """
        framecopy=frame[:]
        m=len(frame)
        n=len(frame[0])
        # framecopy[0][0]=frame[0][0]
        for i in range (1,m):
            framecopy[i][0]+=framecopy[i-1][0]
        for i in range (1,n):
            framecopy[0][i]+=framecopy[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                framecopy[i][j]+=max(framecopy[i-1][j],framecopy[i][j-1])
        return framecopy[-1][-1]