'''
51. 数组中的逆序对

LCR 170. 交易逆序对的总数

在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。请设计一个程序，输入一段时间内的股票交易记录 record,返回其中存在的「交易逆序对」总数。


'''

class Solution(object):
    def reversePairs(self, record):
        """
        :type record: List[int]
        :rtype: int
        """
        def merge_sort(l,r):
            if l>=r:
                return 0
            m=(l+r)//2
            res=merge_sort(l,m)+merge_sort(m+1,r)
            i,j=l,m+1
            tmp[l:r+1]=record[l:r+1]
            for k in range(l,r+1):
                if i==m+1:
                    record[k]=tmp[j]
                    j+=1
                elif j==r+1:
                    record[k]=tmp[i]
                    i+=1
                elif tmp[i]<=tmp[j]:
                    record[k]=tmp[i]
                    i+=1
                else:
                    record[k]=tmp[j]
                    j+=1
                    res+=m-i+1
            return res
        tmp=[0]*(len(record))
        return merge_sort(0,len(record)-1)













