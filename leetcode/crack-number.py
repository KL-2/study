'''
剑指Offer 46. 把数字翻译成字符串
LCR 165. 解密数字

现有一串神秘的密文 ciphertext,经调查,密文的特点和规则如下：

密文由非负整数组成
数字 0-25 分别对应字母 a-z
请根据上述规则将密文 ciphertext 解密为字母，并返回共有多少种解密结果。


'''
class Solution(object):
    def crackNumber(self, ciphertext):
        """
        :type ciphertext: int
        :rtype: int
        """
        num=str(ciphertext)
        n=len(num)
        dp=[1 for _ in range(n+1)]
        for i in range(2,n+1):
            if str(10)<=num[i-2:i]<=str(25):
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        return dp[n]