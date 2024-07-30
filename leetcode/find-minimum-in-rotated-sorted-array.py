# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
# 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

# 给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

# 你必须尽可能减少整个过程的操作步骤。
#leetcode 154 offer 11

#分析：考虑数组中的最后一个元素 x：在最小值右侧的元素，它们的值一定都小于等于 x；而在最小值左侧的元素，它们的值一定都大于等于 x。因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。
'''
LeetCode 第154题 寻找旋转排序数组中的最小值 II

《剑指Offer第2版》第11题 旋转数组的最小数字
'''

class Solution:
    def findmin_Ologn(self,nums):
        low,high=0,len(nums)-1
        while low<high:
            pivot=low+(high-low)//2
            if nums[pivot]<nums[high]:
                high=pivot
            elif nums[pivot]>nums[high]:
                low=pivot+1
            else:
                high-=1
        return nums[low]
# 正确性证明：
# 当 nums[m]=nums[j] 时，无法判定 m在左（右）排序数组，自然也无法通过二分法安全地缩小区间，因为其会导致旋转点 x 不在区间 [i,j]内。
# 而证明 j= j - 1 正确（缩小区间安全性），需分为两种情况：
# 当 x<j 时： 易得执行 j=j-1后，旋转点 x 仍在区间 [i,j]内。
# 当 x=j 时： 执行 j=j- 1 后越过（丢失）了旋转点 x ，但最终返回的元素值 nums[i] 仍等于旋转点值 nums[x]。
# 由于 x=j ，因此 nums[x]=nums[j]=nums[m]≤number[i];
# 又由于 i≤m<j恒成立，因此有 m<x，即此时 m 一定在左排序数组中，因此 nums[m]≥nums[i] ;
# 综合 1. , 2. ，可推出 nums[i]=nums[m]，且区间 [i,m] 内所有元素值相等，即有：
# nums[i]=nums[i+1]=⋯=nums[m]=nums[x]
# 此时，执行 j=j−1 后虽然丢失了旋转点 x ，但之后区间 [i,j]只包含左排序数组，二分下去返回的一定是本轮的 nums[i]，而其与 nums[x]相等。
# 综上所述，此方法可以保证返回值 nums[i] 等于旋转点值 nums[x]，但在少数特例下 i≠x ；而本题目只要求返回 “旋转点的值” ，因此本方法正确。

    def findmin_On(self,nums):
        low,high=0,len(nums)-1
        while low<high:
            pivot=low+(high-low)//2
            if nums[pivot]<nums[high]:
                high=pivot
            elif nums[pivot]>nums[high]:
                low=pivot+1
            else:
                #O(n)
                min=nums[low]
                for i in range (low+1,high+1):
                    if min>nums[i]:
                        min=i
                    return min
        return nums[low]
    
if __name__=="__main__":
    solution=Solution()
    nums=[2,2,2,0,1]
    nums1=[1,3,5]
    print(solution.findmin_Ologn(nums))
    print(solution.findmin_On(nums))
    print(solution.findmin_Ologn(nums1))
    print(solution.findmin_On(nums1))