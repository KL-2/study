'''
剑指Offer第2版 49. 丑数
264. 丑数 II

给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是质因子只包含 2、3 和 5 的正整数。
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[1]*n
        a,b,c=0,0,0
        for i in range(1,n):
            num2,num3,num5=res[a]*2,res[b]*3,res[c]*5
            res[i]=min(num2,num3,num5)
            if res[i]==num2:a+=1
            if res[i]==num3:b+=1
            if res[i]==num5:c+=1
        return res[-1]








