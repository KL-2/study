# LeetCode 第509题 Leetcode 509（斐波那契） 第70题 Leetcode 70 （爬梯子）

# 《剑指Offer第2版》第10-I题 斐波那契 第10-II题 青蛙跳台阶

class Fibonacci:
    def __init__(self) -> None:
        pass
    def fibonacci_DP(self,n):#O(n),O(1)
        if n<2:
            return n
        p,q,r=0,0,1
        for _ in range(2,n+1):#n+1
            p,q=q,r
            r=q+p
        return r
    
    def fibonacci_DP_array(self,n):
        # dp=[0 for i in range(n+1)]
        dp=[0]*(n+1)
        #dp[0]=0
        dp[1]=1
        dp[2]=2
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

if __name__=="__main__":
    fib=Fibonacci()
    print(fib.fibonacci_DP(6))