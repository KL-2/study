'''LCR 139. 训练计划 I

教练使用整数数组 actions 记录一系列核心肌群训练项目编号。为增强训练趣味性，需要将所有奇数编号训练项目调整至偶数编号训练项目之前。请将调整后的训练项目编号以 数组 形式返回。'''
'''《剑指Offer第2版》第21题 调整数组顺序使奇数位于偶数前面'''


class Solution(object):
    def trainingPlan_left_and_right(self, actions):
        """
        :type actions: List[int]
        :rtype: List[int]
        """
        left,right=0,len(actions)-1
        while (left<right):
            if(actions[left]&1!=0):
                left+=1
                continue
            if actions[right]&1==0:
                right-=1
                continue
            c=actions[right]
            actions[right]=actions[left]
            actions[left]=c
        return actions
    def trainingPlan_slow_and_fast(self, actions):
        """
        :type actions: List[int]
        :rtype: List[int]
        """
        slow,fast=0,0
        while(fast<len(actions)):
            if (actions[fast]&1==1):
                actions[fast],actions[slow]=actions[slow],actions[fast]
                slow+=1
            fast+=1
        return actions
    def trainingPlan_On(self,actions):
        even,odd=[],[]
        for action in actions:
            if action&1==1:
                even.append(action)
            else:
                odd.append(action)
        return even+odd
    
if __name__=="__main__":
    solution=Solution()
    a=[1,2,3,4,5]
    print(solution.trainingPlan_left_and_right(a))