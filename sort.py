class Solution:
    def bubblesort(self,nums):
        for i in range(len(nums)-1,0,-1):
            # print(f"i:{i}",end=" ")
            for j in range(i):
                # print(f"j:{j}",end=" ")
                
                if(nums[j]>nums[j+1]):
                    c=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=c
                    print(nums)
        return nums
    
if __name__=="__main__":
    solution=Solution()
    nums=[7,6,1,3,4,5,6]
    print(nums)
    sorted_nums=solution.bubblesort(nums)
    print(sorted_nums)