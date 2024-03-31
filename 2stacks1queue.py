'''读者来到图书馆排队借还书，图书管理员使用两个书车来完成整理借还书的任务。书车中的书从下往上叠加存放，图书管理员每次只能拿取书车顶部的书。排队的读者会有两种操作：

push(bookID)：把借阅的书籍还到图书馆。
pop()：从图书馆中借出书籍。
为了保持图书的顺序，图书管理员每次取出供读者借阅的书籍是 最早 归还到图书馆的书籍。你需要返回 每次读者借出书的值 。

如果没有归还的书可以取出，返回 -1 
https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
'''
'''offer 9 用两个栈实现队列'''
'''栈stack是先进后出,队列queue是先进先出,2个栈可以组成1个队列'''
class Queue:
    def __init__(self) -> None:
        self.stack_for_enqueue=[]
        self.stack_for_dequeue=[]
    def appendTail(self,value):
        self.stack_for_enqueue.append(value)
    def deleteHead(self):
        if self.stack_for_dequeue:#如果dequeue有元素，直接输出
            return self.stack_for_dequeue.pop()
        if not self.stack_for_enqueue:#没有return，dequeue就没有元素，如果enqueue也没有，都为空就返回0
            return -1
        while self.stack_for_enqueue:#如果dequeue没有，enqueue有，先放到dequeue里再输出
            self.stack_for_dequeue.append(self.stack_for_enqueue.pop())
        return self.stack_for_dequeue.pop()
    
def Test1():#正常情况,空队列删除添加元素
    queue=Queue()
    queue.appendTail(10)
    queue.appendTail(8)
    queue.appendTail(9)
    return queue.deleteHead()

def Test2():#为空，空队列删除添加元素
    queue=Queue()
    return queue.deleteHead()

def Test3():#连续输出，直至为空
    queue=Queue()
    queue.appendTail(10)
    queue.deleteHead()
    return queue.deleteHead()

def Test4():
    queue=Queue()
    queue.stack_for_enqueue=[6,8]
    queue.appendTail(10)
    queue.deleteHead()
    return queue.deleteHead()

if "__main__"==__name__:
    print(f"Test1 is {Test1()},correct is 10")
    print(f"Test2 is {Test2()},correct is -1")
    print(f"Test3 is {Test3()},correct is -1")
    print(f"Test3 is {Test4()},correct is 8")
