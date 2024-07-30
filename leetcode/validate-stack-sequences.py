'''946. 验证栈序列

给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

LeetCode 第946题 验证栈序列

《剑指Offer第2版》第31题 栈的压入、弹出序列
LeetCode 第946题 验证栈序列

《剑指Offer第2版》第31题 栈的压入、弹出序列
'''



class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack=[]
        j=0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return len(stack)==0