'''
48. 最长不重复的子
3. 无重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的 最长 
子串的长度。
'''
class Solution(object):
    def lengthOfLongestSubstring_huadongchuangkou(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        res=0
        i=-1
        for j in range(len(s)):
            if s[j] in dic:
                i=max(i,dic[s[j]])
            dic[s[j]]=j
            res=max(res,j-i)
        return res

