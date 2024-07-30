'''
《剑指Offer第2版》第45题 把数组排成最小的数
LCR 164. 破解闯关密码

闯关游戏需要破解一组密码，闯关组给出的有关密码的线索是：

一个拥有密码所有元素的非负整数数组 password
密码是 password 中所有元素拼接后得到的最小的一个数
请编写一个程序返回这个密码。
《剑指Offer第2版》第45题 把数组排成最小的数
'''
class Solution(object):
    def crackPassword(self, password):
        """
        :type password: List[int]
        :rtype: str
        """
        if not password:
            return None
        nums=password[:]
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])>(nums[j]+nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
        return "".join(nums)
'''
根据题目的要求,两个数字m和n能拼接成数字mn和nm,如果mn < nm那么现在他们的相对位置是正确的,如果mn > nm,那么就需要将n移到m的前面,根据这样的特性我们能将整个数组进行排列,得到最终的结果.
我们在比较的时候先将数据转换成str格式的,利用str格式的字符串直接比较就可以

'''