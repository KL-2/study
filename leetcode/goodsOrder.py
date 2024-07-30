'''

《剑指Offer第2版》第38题 字符串的排列

LCR 157. 套餐内商品的排列顺序

某店铺将用于组成套餐的商品记作字符串 goods,其中 goods[i] 表示对应商品。请返回该套餐内所含商品的 全部排列方式 。

返回结果 无顺序要求，但不能含有重复的元素

'''

class Solution(object):
    def goodsOrder(self, goods):
        """
        :type goods: str
        :rtype: List[str]
        """
        arr=list(goods)
        res=[]
        def dfs(x):
            if x==len(arr)-1:
                res.append("".join(arr))
                return
            hmap=set()#要在递归里面
            for i in range(x,len(arr)):
                if arr[i] in hmap:continue#剪枝操作
                hmap.add(arr[i])
                arr[i],arr[x]=arr[x],arr[i]#固定
                dfs(x+1)
                arr[i],arr[x]=arr[x],arr[i]#解锁
        dfs(0)
        return res