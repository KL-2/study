import sys
import random

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
            while(position>=1 and nums[position-1]>value):
                nums[position]=nums[position-1]
                position-=1
                # print(f"position:{position}")
            nums[position]=value
            print(nums)
        return nums

    def shellsort(self,nums):
        print(f"current algorithm:{sys._getframe().f_code.co_name}")
        gap=int(len(nums)/2)
        # print(gap)
        while gap>0:
            for i in range(gap,len(nums)):
                value=nums[i]
                position=i
                while (position>=gap and nums[position-gap]>value):
                    nums[position]=nums[position-gap]
                    position-=gap#已知有序
                nums[position]=value
                # print(f"{position}|{nums}")
            gap=int(gap/2)
            # print(gap)
        return nums

    def mergesort(self,nums):
        
        def merge(nums,left,mid,right):
            nums_=[]
            #nums[left:right+1] 表示从索引 left 开始到索引 right 结束的子数组。 
            i,j=left,mid+1
            while i<=mid and j<=right:
                if nums[i]<=nums[j]:
                    nums_.append(nums[i])
                    i+=1
                else:
                    nums_.append(nums[j])
                    j+=1
            while i<=mid :
                nums_.append(nums[i])
                i+=1
            while j<=right:
                nums_.append(nums[j])
                j+=1
            nums[left:right+1] = nums_
        #不用return改值就行
                    
        def mergesort_(nums,left,right):
            if(left>=right):
                return nums
            mid=left+(right-left)//2
            mergesort_(nums,left,mid)
            mergesort_(nums,mid+1,right)
            merge(nums,left,mid,right)
            return nums

        left,right=0,len(nums)-1
        sorted_nums=mergesort_(nums,left,right)
        print(sorted_nums)
        return sorted_nums
 
    def mergesort1(self,nums): 
        def merge(nums,left,mid,right):
            #写法一
            # nums_=nums[:]
            #代码一顿就在这
            #如果是nums_=nums二者指向的是同一个地址，一起更改
            #写法二
            nums_=[0]*len(nums)
            nums_[left:right+1]=nums[left:right+1] 
            #nums[left:right+1] 表示从索引 left 开始到索引 right 结束的子数组。 
            i,j,k=left,mid+1,0
            while i<=mid and j<=right:
                if nums[i]<=nums[j]:
                    nums_[left+k]=nums[i]
                    i+=1
                    k+=1
                else:
                    nums_[left+k]=nums[j]
                    j+=1
                    k+=1
            if i<=mid:
                nums_[left+k:right+1]=nums[i:mid+1]
            else:
                nums_[left+k:right+1]=nums[j:right+1]
            nums[left:right+1]=nums_[left:right+1]
        
        def mergesort_(nums,left,right):
            if(left>=right):
                return nums[left:right+1]
            mid=left+(right-left)//2
            mergesort_(nums,left,mid)
            mergesort_(nums,mid+1,right)
            merge(nums,left,mid,right)
            return nums[left:right+1]

        left,right=0,len(nums)-1
        sorted_nums=mergesort_(nums,left,right)
        # print(sorted_nums)
        return sorted_nums

    def quicksort(self,nums):
        def partition(nums,left,right):
            pivotindex=random.randint(left,right)
            pivot=nums[pivotindex]
            self.swapnums(nums,pivotindex,left)
            index=left+1
            for i in range(left+1,right+1):
                if nums[i]<pivot:
                    self.swapnums(nums,i,index)
                    index+=1
            self.swapnums(nums,left,index-1)
            return index-1
            
        def quicksort_(nums,left=None,right=None):
            left=0 if not isinstance(left,(int,float)) else left
            right=len(nums)-1 if not isinstance(right,(int,float)) else right
            if left<right:
                partitionindex=partition(nums,left,right)
                quicksort_(nums,left,partitionindex-1)
                quicksort_(nums,partitionindex+1,right)
            return nums
        sorted_nums=quicksort_(nums)
        return sorted_nums

    def heapsort(self,nums):
        def heapify(nums,len,i):
            left=2*i+1
            right=2*i+2
            largest=i
            if (left<len and nums[left]>nums[largest]):
                largest=left
            if (right<len and nums[right]>nums[largest]):
                largest=right
            if i!=largest:# change root,if needed
                self.swapnums(nums,i,largest)
                #heapify the root
                heapify(nums,len,largest)#这一步只在不等时执行否则死循环
        def heapsort_(nums):
            #build a maxheap
            for i in range(len(nums)//2-1,-1,-1):
                heapify(nums,len(nums),i)
            # one by one extract elements
            for i in range(len(nums)-1,0,-1):
                self.swapnums(nums,i,0)
                heapify(nums,i,0)
            return nums
        sorted_nums=heapsort_(nums)
        return sorted_nums

    def countingsort(self,nums):
        maxvalue=max(nums)
        minvalue=min(nums)
        bucketlen=maxvalue-minvalue+1
        bucket=[0]*bucketlen
        sorted_nums=[0]*len(nums)
        for i in nums:
            if not bucket[i-minvalue]:
                bucket[i-minvalue]=0
            bucket[i-minvalue]+=1
        sortedindex=0
        for i in range(bucketlen):
            while bucket[i-minvalue]>0:
                sorted_nums[sortedindex]=i
                sortedindex+=1
                bucket[i-minvalue]-=1    
        return sorted_nums

if __name__=="__main__":
    solution=Solution()
    random.seed(58)
    arr = [random.randint(0,100) for _ in range(10)]
    # arr=[4,3,2,5]
    print("input:", arr)
    sorted_arr=solution.countingsort(arr)
    print("result:", sorted_arr)