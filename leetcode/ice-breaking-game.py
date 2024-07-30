'''
剑指Offer第2版 62. 圆圈中最后剩下的数字

LCR 187. 破冰游戏

社团共有 num 位成员参与破冰游戏，编号为 0 ~ num-1。成员们按照编号顺序围绕圆桌而坐。社长抽取一个数字 target,从 0 号成员起开始计数，排在第 target 位的成员离开圆桌，且成员离开后从下一个成员开始计数。请返回游戏结束时最后一位成员的编号。

'''

class Solution(object):
    def iceBreakingGame(self, num, target):
        """
        :type num: int
        :type target: int
        :rtype: int
        """
        nums=[i for i in range(num)]
        size=num
        start=0#0开始
        while size!=1:
            i=(start+target-1)%size
            nums.pop(i)
            start=i#别忘了更新start
            size-=1
        return nums.pop()