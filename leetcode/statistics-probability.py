'''
剑指Offer第2版 60. n个骰子的点数

LCR 185. 统计结果概率

你选择掷出 num 个色子，请返回所有点数总和的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 num 个骰子所能掷出的点数集合中第 i 小的那个的概率。

'''

class Solution(object):
    def statisticsProbability(self, num):
        """
        :type num: int
        :rtype: List[float]
        """
        dp=[1/6]*6
        for i in range(2,num+1):
            tmp=[0]*(5*i+1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j+k]+=dp[j]/6#这里是j
            dp=tmp
        return dp

if __name__=="__main__":
    solution=Solution()
    num=2
    print(solution.statisticsProbability(num))
