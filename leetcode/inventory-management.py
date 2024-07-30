'''
《剑指Offer第2版》第40题 最小的k个数

LCR 159. 库存管理 III

仓库管理员以数组 stock 形式记录商品库存表，其中 stock[i] 表示对应商品库存余量。请返回库存余量最少的 cnt 个商品余量，返回 顺序不限。
《剑指Offer第2版》第40题 最小的k个数
'''

class Solution(object):
    def inventoryManagement(self, stock, cnt):
        """
        :type stock: List[int]
        :type cnt: int
        :rtype: List[int]
        """
        if cnt>=len(stock):
            return stock
        def quick_sort(l,r):
            i,j=l,r
            while i<j:
                while i<j and stock[j]>=stock[l]:
                    j-=1
                while i<j and stock[i]<=stock[l]:
                    i+=1
                #两个while不能换顺序，解释：哈喽，文中的写法这两个 while执行完， i j 同时指向一个 < arr[l] 的数，因此最后再执行 arr[l], arr[i] = arr[i], arr[l] 可以把哨兵交换到正确的位置。 而如果互换这两句，那么就是 i 先向右遍历，两个 while 执行完， i j 同时指向一个 > arr[l] 的数，那么就不对了。如果要交换写，那么同时也要把哨兵换成数组的末元素，让整个哨兵划分操作对称。
                stock[i],stock[j]=stock[j],stock[i]
            stock[i],stock[l]=stock[l],stock[i]
            if i>cnt:#顺序滤清
                return quick_sort(l,i-1)
            if i<cnt:
                return quick_sort(i+1,r)
            return stock[:cnt]#无序
        return quick_sort(0,len(stock)-1)#记得return