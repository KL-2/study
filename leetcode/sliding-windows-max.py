'''
239. 滑动窗口最大值

给你一个整数数组 nums,有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

'''


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums and k==0:
            return []
        deque=collections.deque()
        for i in range(k):
            while deque and deque[-1]<nums[i]:
                deque.pop()
            deque.append(nums[i])
        res=[]
        res.append(deque[0])
        for i in range(k,len(nums)):
            if deque[0]==nums[i-k]:#不能有窗口内的元素
                deque.popleft()
            while deque and deque[-1]<nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res



''''
 剑指Offer第2版 59-2. 队列的最大值

LCR 184. 设计自助结算系统

请设计一个自助结账系统，该系统需要通过一个队列来模拟顾客通过购物车的结算过程，需要实现的功能有：

get_max()：获取结算商品中的最高价格，如果队列为空，则返回 -1
add(value)：将价格为 value 的商品加入待结算商品队列的尾部
remove()：移除第一个待结算的商品价格，如果队列为空，则返回 -1
注意，为保证该系统运转高效性，以上函数的均摊时间复杂度均为 O(1)
'''

class Checkout(object):

    def __init__(self):
        self.deque=collections.deque()
        self.max_deque=collections.deque()



    def get_max(self):
        """
        :rtype: int
        最大值
        使用双端队列的头总是存最大值

        """
        if self.max_deque:
            return self.max_deque[0]
        else:
            return -1




    def add(self, value):
        """
        :type value: int
        :rtype: None
        入队
        保证队头总是当前最大值
        如果下一个数小于当前最大值，也放入这个双端队列后面。这样保证了，当原最大值被弹出后，有后续值跟上
        如果遇到一个比当前最大值大的数，弹出双端队列里所有数，再把他放入

        """
        self.deque.append(value)
        while self.max_deque and self.max_deque[-1]<value:
            self.max_deque.pop()
        self.max_deque.append(value)



    def remove(self):
        """
        :rtype: int
        出队
        原数列出队的同时，最大数列的头也要出队
        """
        if not self.deque:
            return -1
        if self.max_deque[0]==self.deque[0]:
            self.max_deque.popleft()
        return self.deque.popleft()





# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()