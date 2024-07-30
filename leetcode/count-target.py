'''
53-1. 两链表的公共节点
LCR 172. 统计目标成绩的出现次数
某班级考试成绩按非严格递增顺序记录于整数数组 scores,请返回目标成绩 target 的出现次数。

'''
class Solution(object):
    def countTarget(self, scores, target):
        """
        :type scores: List[int]
        :type target: int
        :rtype: int
        """
        def helper(tar):
            i,j=0,len(scores)-1
            while i<=j:#要i>j再结束
                m=(i+j)//2
                if scores[m]<=tar:#先i后j#while是i>j退出
                    i=m+1
                else:
                    j=m-1
            return i
        return helper(target)-helper(target-1)