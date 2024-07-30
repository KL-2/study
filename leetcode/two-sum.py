'''
剑指Offer第2版 57-1. 和为s的两个数字

LCR 179. 查找总价格为目标值的两个商品

购物车内的商品价格按照升序记录于数组 price。请在购物车中找到两个商品的价格总和刚好是 target。若存在多种情况,返回任一结果即可。


'''
class Solution(object):
    def twoSum(self, price, target):
        """
        :type price: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j=0,len(price)-1
        while i<j:
            sum=price[i]+price[j]
            if sum<target:#因为升序
                i+=1
            elif sum>target:
                j-=1
            else:
                return price[i],price[j]
        return []
'''
剑指Offer第2版 57-2. 和为s的连续正数序列
LCR 180. 文件组合

待传输文件被切分成多个部分，按照原排列顺序，每部分文件编号均为一个 正整数（至少含有两个文件）。传输要求为：连续文件编号总和为接收方指定数字 target 的所有文件。请返回所有符合该要求的文件传输组合列表。

注意，返回时需遵循以下规则：

每种组合按照文件编号 升序 排列；
不同组合按照第一个文件编号 升序 排列。
'''
class Solution(object):
    def fileCombination(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i,j,s=1,2,3
        res=[]
        while i<j:
            if s==target:
                res.append(list(range(i,j+1)))
            if s>=target:
                s-=i
                i+=1
            else:#顺序无所谓的
                j+=1
                s+=j#要加的是j+1的值
        return res









