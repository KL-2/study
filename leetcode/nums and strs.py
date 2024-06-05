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
        # 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
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

    def rotate(self,matrix):
        # 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
        for matrix_ in matrix:
            if not isinstance(matrix_,list):
                    return -1
            for matrix__ in matrix_:
                if not isinstance(matrix__,int):
                    return -1
        row=len(matrix)
        col=len(matrix[0])
        matrixnew=[[0]*row for _ in range(col)]#旋转后形状
        for i in range(row):#遍历原矩阵
            for j in range(col):
                matrixnew[j][row-i-1]=matrix[i][j]
                #matrixnew[0][row]=matrix[0][0]
        matrix[:]=matrixnew#这里形状改变了也ok
        return matrix
    
    def rotate_better(self,matrix):
        # 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
        #无需重建新的数组
        for matrix_ in matrix:
            if not isinstance(matrix_,list):
                    return -1
            for matrix__ in matrix_:
                if not isinstance(matrix__,int):
                    return -1
        row=len(matrix)
        col=len(matrix[0])
        if row!=col:
            return -1
        for i in range(row//2):#遍历原矩阵
            for j in range((col+1)//2):
                matrix[i][j],matrix[row-j-1][i],matrix[row-i-1][row-j-1],matrix[j][row-i-1]=matrix[row-j-1][i],matrix[row-i-1][row-j-1],matrix[j][row-i-1],matrix[i][j]
                #matrix[j][row-i-1]=matrix[i][j]
                #不能拆开
        return matrix

    def rotate_1(self,matrix):
        # 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
        for matrix_ in matrix:
            if not isinstance(matrix_,list):
                    return -1
            for matrix__ in matrix_:
                if not isinstance(matrix__,int):
                    return -1
        row=len(matrix)
        col=len(matrix[0])
        if row!=col:
            return -1
        #水平翻转
        for i in range(row//2):
            for j in range(col):
                matrix[row-i-1][j],matrix[i][j]=matrix[i][j],matrix[row-i-1][j]
                #顺序无所谓，不能拆开就是同时换，之前遇到的不要包括在内
                # matrix[i][j],matrix[row-i-1][j]=matrix[row-i-1][j],matrix[i][j]
        #对角线翻转
        for i in range(row):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix


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
    matrixlist_rotate=[
            [[[1,2,3],
              [4,5,6],
              [7,8,9]],
             [[7,4,1],
              [8,5,2],
              [9,6,3]]],#N*N
            [[[1,2,3],
              [4,5,6]],
             [[4,1],
              [5,2],
              [6,3]]],#N1*N2
            [[[9,'4'],5,"$"],-1],#错误输入
    ]
    matrixlist_rotate1=[
            [[[1,2,3],
              [4,5,6],
              [7,8,9]],
             [[7,4,1],
              [8,5,2],
              [9,6,3]]],#N*N
            [[[1,2,3],
              [4,5,6]],
             -1],#N1*N2
            [[[9,'4'],5,"$"],-1],#错误输入
    ]

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
    # for nums in numslist_mergeintervals:
    #     if solution.mergeintervals(nums[0])!=nums[1]:
    #         print(nums[0],solution.mergeintervals(nums[0]),'correct is ',nums[1]) 
    #         ALLCORRECT=False
    # for matrix in matrixlist_rotate:
    #     if solution.rotate(matrix[0])!=matrix[1]:
    #         print(matrix[0],solution.rotate(matrix[0]),'correct is ',matrix[1]) 
    #         ALLCORRECT=False
    # for matrix in matrixlist_rotate1:
    #     if solution.rotate_better(matrix[0])!=matrix[1]:
    #         print(matrix[0],solution.rotate_better(matrix[0]),'correct is ',matrix[1]) 
    #         ALLCORRECT=False
    for matrix in matrixlist_rotate1:
        if solution.rotate_1(matrix[0])!=matrix[1]:
            print(matrix[0],solution.rotate(matrix[0]),'correct is ',matrix[1]) 
            ALLCORRECT=False
    
    if (ALLCORRECT==True):
        print("all correct!")
        print("say my name!")
