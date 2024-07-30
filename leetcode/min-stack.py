'''155. 最小栈

设计一个支持 push ,pop ,top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素

LeetCode 第155题 最小栈

《剑指Offer第2版》第30题 包含min函数的栈
LeetCode 第155题 最小栈

《剑指Offer第2版》第30题 包含min函数的栈
'''


class Minstack:
    def __init__(self) :
        self.data=[]
        self.helper=[]
    def push(self,val):
        self.data.append(val)
        if len(self.helper)==0 or val<self.helper[-1]:
            self.helper.append(val)
        else:
            self.helper.append(self.helper[-1])
    def pop(self):
        self.data.pop()
        self.helper.pop()
    def top(self):
        if self.data:
            return self.data[-1]
    def minstack(self):
        if self.helper:
            return self.helper[-1]








    