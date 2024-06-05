'''
LeetCode 第50题 Pow(x, n)

《剑指Offer第2版》第16题 数值的整数次方
'''
#实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。

class Solution:
    def mypow_recursive(self,x,n):
        def quickMul(n):
            if n==0:
                return 1.0
            y=quickMul(n//2)
            if n%2==0:
                return y*y
            else:
                return y*y*x
        if n>=0:
            return quickMul(n)
        else:
            return 1.0/quickMul(-n)
        
    def mypow_iterate(self,x,n):
        #x**77恰好77二进制(1001101)2
        #（1，4，8，64）刚好是二进制中1对应
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__=="__main__":
    solution=Solution()
    print(solution.mypow_recursive(2,2))
    print(solution.mypow_iterate(2,2))