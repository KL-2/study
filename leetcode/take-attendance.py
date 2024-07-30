'''

剑指Offer第2版 53-2. 0 ~ n-1中缺失的数
LCR 173. 点名

某班级 n 位同学的学号为 0 ~ n-1。点名结果记录于升序数组 records。假定仅有一位同学缺席,请返回他的学号。


'''
class Solution(object):
    def takeAttendance(self, records):
        """
        :type records: List[int]
        :rtype: int
        """
        i,j=0,len(records)-1
        while i<=j:
            m=(i+j)//2
            if records[m]==m:
                i=m+1
            else:
                j=m-1
        return i
    

