'''
LeetCode 第295题 数据流的中位数

《剑指Offer第2版》第41题 数据流中的中位数
LeetCode 第295题 数据流的中位数

《剑指Offer第2版》第41题 数据流中的中位数
295. 数据流的中位数
困难

中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
'''
'''
import heapq
a = []   #创建一个空堆
heapq.heappush(a,18)
提供了小根堆（从小到大）
如果想整一个大根堆（从大到小）就加符号
a = []
for i in [1, 5, 20, 18, 10, 200]:
    heapq.heappush(a,-i)
print(list(map(lambda x:-x,a)))
heappushpop(h,4) #增加4同时删除最小值2并返回该最小值
'''
from heapq import *
class MedianFinder(object):

    def __init__(self):
        self.A=[]#小顶堆
        self.B=[]#大顶堆

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.A)==len(self.B):
            heappush(self.A,-heappushpop(self.B,-num))#和B有联系的都要加-号
        else:
            heappush(self.B,-heappushpop(self.A,num))


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.A)==len(self.B):
            return (self.A[0]-self.B[0])/2.
        else:
            return self.A[0]
