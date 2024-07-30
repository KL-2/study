'''
LeetCode 第400题 第N个数字

《剑指Offer第2版》第44题 数字序列中某一位的数字

400. 第 N 位数字

给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位上的数字。

'''
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit=1
        count=9
        start=1
        while n>count:
            n-=count
            digit+=1
            start*=10
            count=9*start*digit#=不是+=
        num=start+(n-1)//digit
        return int(str(num)[(n-1)%digit])
    