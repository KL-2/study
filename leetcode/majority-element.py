'''
LeetCode 第169题 多数元素

《剑指Offer第2版》第39题 数组中出现次数超过一半的数字

169. 多数元素

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''

class Solution(object):
    def majorityElement_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]
    
    def majorityElement_hash(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash={}
        limit=len(nums)/2
        for x in nums:
            if x not in hash:
                hash[x]=1
            else:
                hash[x]+=1
            if hash[x]>limit:#一定要放到循环里，要不还得再写个循环逻辑才对
                return x
        return None

    def majorityElement_vote(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        majority=nums[0]
        for x in nums[1:]:#要加[1:]#误例：nums =[6,5,5]
            if count==0:
                majority=x
            if majority==x:
                count+=1
            else:
                count-=1
        return majority