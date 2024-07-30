'''
LeetCode 第53题 最大子序和

《剑指Offer第2版》第42题 连续子数组的最大和

53. 最大子数组和

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组
是数组中的一个连续部分。
LeetCode 第53题 最大子序和

《剑指Offer第2版》第42题 连续子数组的最大和


'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numscopy=nums[:]#不能直接赋值，就相当于没做
        for i in range(1,len(numscopy)):
            numscopy[i]+=max(numscopy[i-1],0)
        return max(numscopy)