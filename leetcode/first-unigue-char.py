'''
剑指Offer第2版 50. 第一个只出现一次的字符

387. 字符串中的第一个唯一字符

给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        position=dict()
        n=len(s)
        for i,ch in enumerate(s):
            if ch in position:
                position[ch]=-1
            else:
                position[ch]=i
        first=n
        for pos in position.values():
            if pos!=-1 and pos<first:
                first=pos
        if first==n:
            return -1
        return first




