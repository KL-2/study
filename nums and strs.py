class Solution(object):
    def pivotIndex(self, nums):
        """
        寻找数组的中心索引
        给你一个整数数组 nums ，请计算数组的 中心下标 。
        数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
        如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
        如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
        """
        for num in nums:
            if not isinstance(num,int):
                return -1
        right=0
        totalnumber=sum(nums)
        for i in range(len(nums)):
            left=totalnumber-right-nums[i]
            if left==right:
                return i
            right+=nums[i]
        return -1
    
    def searchInsert(self, nums, target):
        """
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
        输入数组排好序且无重复元素
        """
        if not isinstance(target,int):
            return -1
        for i in nums:
            if not isinstance(i,int):
                return -1
            
        if not nums or len(nums)!=len(set(nums)) or nums!=sorted(nums,reverse=False) :#数组为空，重复数字和升序，降序为sorted(nums,reverse=True)
            return -1

        i=0
        result=0
        while i <len(nums) and nums[i]<=target:#注意and顺序问题
            if nums[i]==target:
                return i
            i+=1 
            result=i
        return result
    
    def mergeintervals(self,intervals):
        for interval in intervals:
            if not isinstance(interval,list) or len(interval)!=2:
                    return -1
            for interval_ in interval:
                if not isinstance(interval_,int):
                    return -1
            if (interval[0]>interval[1]):
                return -1
        intervals.sort(key=lambda x:x[0])
        merged=[]
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else :
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged

if __name__=="__main__":
    numslist_pivotIndex=[
              [[0],0],#单输入
              [[],-1],#空
              [[5,"$"],-1],#错误输入
              [[0,1,0,0,0,1,0],2],#多个中心索引
              [[-1,1,0],2]]#右侧
    numslist_searchinsert=[
              [[0],0,0],
              [[0],1,1],
              [[],0,-1],#空
              [[5,"$"],5,-1],#错误输入
              [[5,1,0],5,-1],#错误输入
              [[1,2,3],'p',-1],#错误输入
              [[-1,1,10],-2,0]]
    numslist_mergeintervals=[
              [[[1,6],[4,5],[7,8]],[[1,6],[7,8]]],#有重叠，且包含
              [[[1,6],[4,7],[7,8]],[[1,8]]],#有重叠，不包含
              [[[1,3],[4,5],[7,8]],[[1,3],[4,5],[7,8]]],#不重叠
              [[],[]],#空
              [[[1,1]],[[1,1]]],#元素相等
              [[[9,4]],-1],#错误输入
              [[[9,'4'],5,"$"],-1],#错误输入
              [[[[3,4],[5,6]]],-1],#错误嵌套
              [[[1,7]],[[1,7]]]]#单个区间
    solution=Solution()
    ALLCORRECT=True
    # for nums in numslist_pivotIndex:
        # if solution.pivotIndex(nums[0])!=nums[1]:
        #     print(nums[0],solution.pivotIndex(nums[0]),'correct is ',nums[1]) 
        #     ALLCORRECT=False
    # for nums in numslist_searchinsert:
    #     if solution.searchInsert(nums[0],nums[1])!=nums[2]:
    #         print(nums[0],nums[1],solution.searchInsert(nums[0],nums[1]),'correct is ',nums[2]) 
    #         ALLCORRECT=False
    for nums in numslist_mergeintervals:
        if solution.mergeintervals(nums[0])!=nums[1]:
            print(nums[0],solution.mergeintervals(nums[0]),'correct is ',nums[1]) 
            ALLCORRECT=False

    if (ALLCORRECT==True):
        print("all correct!")
        print("say my name!")
