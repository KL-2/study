'''LeetCode 第191题 位1的个数

《剑指Offer第2版》第15题 二进制中1的个数'''

'''编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中 
设置位
 的个数（也被称为汉明重量）。'''


class Solution(object):
    def hammingWeight_bit_Ok_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while(n):
            if n&1:
                count+=1
            n=n>>1
        return count
    def hammingWeight_bit_Ok_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        count=sum(1 for i in range(32) if n&(2**i))
        return count
    def hammingWeight_bit_Ok_3(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        count=sum(1 for i in range(32) if n&(1<<i))
        return count
    def hammingWeight_bit_Ologn(self, n):
        #位运算优化：n&(n-1)使得最右端1反转
        """
        :type n: int
        :rtype: int
        """
        count=0
        while(n):
            n=n&(n-1)
            count+=1
        return count
    
if __name__=="__main__":
    solution=Solution()
    print(solution.hammingWeight_bit_Ok_1(5))
    print(solution.hammingWeight_bit_Ok_2(5))
    print(solution.hammingWeight_bit_Ok_3(5))
    print(solution.hammingWeight_bit_Ologn(5))