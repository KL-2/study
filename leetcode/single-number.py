'''
剑指Offer第2版 56-1. 数出现次数

260. 只出现一次的数字 III

给你一个整数数组 nums,其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。

'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # XOR result of the entire array
        #所有数做异或：因为上述的异或运算性质，我们可以知道，如果拿 0 和 所有数异或，那么结果就是那个出现一次的数。因为，所有出现两次的数，异或（交换、结合后）都为 0就是a^b
        xor_num = 0
        for num in nums:
            xor_num = xor_num ^ num

        # Find the first (low to high bits) different bit
        #找到第一个不同的位：因为不同的两个数，在二进制中至少有一位是不同的，即存在一个位，其中为0，另一个就为1。
        bit = 1
        while xor_num & bit == 0:
            bit = bit << 1

        # Divide into two groups and find n1, n2
        #利用不同位，将原数组分位两组数。
        #在两组内，分别做异或运算：找到两组内不同的某一个数
        n1, n2 = 0, 0
        for num in nums:
            if num & bit == 0:  # Group 1
                n1 = n1 ^ num
            else:               # Group 2
                n2 = n2 ^ num

        return [n1, n2]
    
'''
剑指Offer第2版 56-2. 数出现次数

137. 只出现一次的数字 II

给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。
'''

class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in range(32):
            total=0
            for num in nums:
                total+=(num>>i)&1
            #total=sum((num>>i)&1 for num in nums)
            if total%3!=0:
                if i==31:
                    res-=(1<<i)
                else:
                    res|=(1<<i)
        return res