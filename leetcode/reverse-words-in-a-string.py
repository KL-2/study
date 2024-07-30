'''
剑指Offer第2版 58-1. 翻转单词顺序

151. 反转字符串中的单词

给你一个字符串 s ，请你反转字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.strip().split()[::-1])#strip()去首位空格,split()切片,[::-1]倒序，[::]全部,[:]全部
    
'''
58-2. 左旋转字符串
'''
class Solution2(object):
    def dynamicPassword(self, password, target):
        """
        :type password: str
        :type target: int
        :rtype: str
        """
        return password[target:]+password[:target]