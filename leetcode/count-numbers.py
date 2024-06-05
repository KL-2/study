# LCR 135. 报数
# 《剑指Offer第2版》第17题 打印从1到最大的n位数
# 实现一个十进制数字报数程序，请按照数字从小到大的顺序返回一个整数数列，该数列从数字 1 开始，到最大的正整数 cnt 位数字结束。

class Solution(object):
    def countNumbers(self, cnt):
        """
        :type cnt: int
        :rtype: List[int]
        """
        return list(range(1,10**cnt))
    
if __name__=="__main__":
    solution=Solution()
    print(solution.countNumbers(2))
