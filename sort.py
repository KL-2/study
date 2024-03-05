import sys

class Solution:
    def swapnums(self,nums,a,b):
        # c=nums[a]
        # nums[a]=nums[b]
        # nums[b]=c
        nums[a],nums[b]=nums[b],nums[a]

    def swapindex(self,a,b):
        a,b=b,a

    def bubblesort(self,nums):
        print(f"current algorithm:{sys._getframe().f_code.co_name}")
        # 比较相邻的两个元素，将大的元素交换到后面，
        # 相当于依次挑出未排序数组中最大元素放到最后面
        for i in range(len(nums)-1,0,-1):#-1是因为nums[j+1]
            for j in range(i):         
                if(nums[j]>nums[j+1]):
                    self.swapnums(nums,j,j+1)
                    print(nums)
        return nums
    
    def selectionsort(self,nums):
        # 找出最小的直接交换
        print(f"current algorithm:{sys._getframe().f_code.co_name}")
        for i in range(len(nums)-1):
            min=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min]:
                    min=j
            if i!=min:
                self.swapnums(nums,i,min)
                print(nums)
        return nums

    def insertionsort(self,nums):
        print(f"current algorithm:{sys._getframe().f_code.co_name}")
        for i in range(1,len(nums)):
            # print(f"i:{i}")
            value=nums[i]
            position=i
            while(position>0 and nums[position-1]>value):
                nums[position]=nums[position-1]
                position-=1
                # print(f"position:{position}")
            nums[position]=value
            print(nums)
        return nums



if __name__=="__main__":
    solution=Solution()
    nums=[7,8,6,6,3,3,1]
    print(f"input is {nums}")
    sorted_nums=solution.insertionsort(nums)
    print(sorted_nums)