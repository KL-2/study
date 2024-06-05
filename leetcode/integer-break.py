'''leetcode 343 整数拆分
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回 你可以获得的最大乘积 。'''
'''LeetCode 第343题 整数拆分

《剑指Offer第2版》第14-I题 剪绳子

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
'''

class Solution(object):
    def integerBreak_dp_On2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        for i in range(2,n+1):
            for j in range (i):
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j])
                #不切，切一次，切更多次
        return dp[n]
    def integerBreak_dp_On(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        if n<3:
            return n-1
        dp[2]=1
        for i in range(3,n+1):
            dp[i]=max(2*(i-2),2*dp[i-2],3*(i-3),3*dp[i-3])
        return dp[n]
    def integerBreak_math_O1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n-1

        quotient,remainder=n//3,n%3
        if remainder==0:
            return 3**quotient
        elif remainder==1:
            return 3**(quotient-1)*4
        else:
            return 3**quotient*2
    
if __name__=="__main__":
    solution=Solution()
    print(solution.integerBreak_dp_On(3))
    print(solution.integerBreak_dp_On2(5))
    print(solution.integerBreak_math_O1(5))
