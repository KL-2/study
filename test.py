# LCR120
# 设备中存有 n 个文件，文件 id 记于数组 documents。
# 若文件 id 相同，则定义为该文件存在副本。请返回任一存在副本的文件 id。
class Solution(object):
    def findRepeatDocument(self, documents):
        """
        :type documents: List[int]
        :rtype: int
        """
        for i in range(len(documents)-1):#0,1,2,3,...,len(documents)-1
            for j in range(i+1,len(documents)):
                if documents[i]==documents[j]:
                    return documents[i]
    
    def findRepeatDocument_sort(self,documents):
        documents.sort()
        pre = documents[0]
        for i in range(1,len(documents)):#跳过自己
            if pre==documents[i]:#和比较documents[i+1]==documents[i]一样
                return documents[i]
            pre=documents[i]

    def findRepeatDocument_haxi(self,documents):
        dict={}
        # for i in range(len(documents)):
        #     if documents[i] not in dict:
        #         dict[i]=0 # here
        #     else:
        #         return documents[i]
        for i in documents:#index的话就是range，如果都使用内容
            if i not in dict:
                dict[i]=1#=啥都行
            else :
                # print(dict,i)
                return i

        

    def findRepeatDocument_erfen(self,documents):
        def judge(mid):
            count = 0
            for num in documents:
                if num <= mid:
                    count += 1
            return count
        
        def binary_search(left, right):
            if left >= right:
                return left
            
            mid = left + (right - left) // 2
            
            count=judge(mid)
            print(f"({left},{mid},{right})",count)
            if count <= mid-left+1:#有问题
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid)
        
        return binary_search(0, len(documents) - 1)


        
    
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
    doc=[3,4,2,1,1,0]
    solution=Solution()
    a=solution.findRepeatDocument_erfen(doc)
    print(f"a:{a}")







