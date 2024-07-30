'''
63. 股票的最大利润
121. 买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。


'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprice=0
        minprice=int(1e9)#1000000000
        for price in prices:
            maxprice=max(maxprice,price-minprice)
            minprice=min(price,minprice)
        return maxprice