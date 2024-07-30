'''
233. 数字 1 的个数

给定一个整数 n,计算所有小于等于 n 的非负整数中数字 1 出现的个数。
LeetCode 第233题 数字 1 的个数

《剑指Offer第2版》第43题 1~n整数中1出现的次数
'''
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        digit=1
        low=0
        cur=n%10
        high=n//10
        while cur!=0 or high!=0:# 当 high 和 cur 同时为 0 时，说明已经越过最高位，因此跳出
            #注意是cur

            if cur==0:
                res+=high*digit
            elif cur==1:
                res+=high*digit+low+1
            else:
                res+=(high+1)*digit
            low+=digit*cur
            cur=high%10
            high//=10
            digit*=10
        return res
    