# LCR120 LCR 120. 寻找文件副本
# 剑指Offer第2版 3. 数组中重复的数字
# 设备中存有 n 个文件，文件 id 记于数组 documents。
# 若文件 id 相同，则定义为该文件存在副本。请返回任一存在副本的文件 id。
class Solution(object):
    def findRepeatDocument(self, documents):
        """
        :type documents: List[int]
        :rtype: int
        """
        documentslist=[]
        for i in range(len(documents)-1):#0,1,2,3,...,(len(documents)-1)-1
            for j in range(i+1,len(documents)):
                if documents[i]==documents[j]:
                    documentslist.append(documents[i])
        return documentslist
    
    def findRepeatDocument_sort(self,documents):
        documents.sort()
        documentslist=[]
        for i in range(0,len(documents)-1):#-1是因为i+1
            if documents[i]==documents[i+1]:
                documentslist.append(documents[i])
        return documentslist
            
    def findRepeatDocument_haxi(self,documents):
        dict={}
        for i in documents:
            if i not in dict:   
                dict[i]=0
            else:
                print(i)
                return i

    def findRepeatDocument_haxi_findall(self,documents):
        mydict={i:0 for i in documents}
        #{}-字典，键值对
        #[]-列表
        #()-元组，创建后不能修改
        for i in documents:#index的话就是range，如果都使用内容
            # if i not in dict:
            mydict[i]+=1#=啥都行
            # else :
            #     # print(dict,i)
            #     return i
        print(mydict)
        sort_dict=dict(sorted(mydict.items(),key=lambda item: item[0]))
        for i in sort_dict:
            if sort_dict[i] != 0:
                print(f"{i}:{sort_dict[i]}")

        

    def findRepeatDocument_erfen(self,documents):
        #数组长度n+1,所有数字1~n
        def judge(mid):
            count = 0
            for num in documents:
                if num <= mid:
                    count += 1
            return count
        
        def binary_search(left, right):
            #不能找出所有重复的数字，[2,2]就不行，
            # 能确定（1，2）有两个但不能确定是谁重复的
            if left >= right:
                return left            
            mid = left + (right - left) // 2
            
            count=judge(mid)
            print(f"({left},{mid},{right})",count)
            if count <= mid-left+1:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid)
        
        return binary_search(1, len(documents) - 1)

    
    def findRepeatDocument_jiaohuan(self,documents):
        for i in range (len(documents)):
            while i!=documents[i]:#这个是while

                #主要目的就是排序排成[0, 1, 2, 3,这种
                if documents[i]==documents[documents[i]]:
                    return documents[i]
                print(f"i={i}")
                print(f"\nbefore:")
                print(documents)
                #主要目的，争取把index是i的干成
                documents[documents[i]],documents[i]\
                    =documents[i],documents[documents[i]]
                #就是交换，注意documents[i]一定要放在后面
                #这里特别重要，不能先把documents[i]赋值了
                #死循环
                # documents[i],documents[documents[i]]\
                #     =documents[documents[i]], documents[i]
                #确实是先等号右侧全搞完再左侧，
                print(f"after:")
                print(documents)
                #交换顺序后不行,进入到了while的死循环
        return None

if __name__=='__main__':
    doc=[3,4,2,1,0,3,1,0]
    solution=Solution()
    a=solution.findRepeatDocument_jiaohuan(doc)
    # print(f"a:{a}")







